/**
 * nexus-orchestrator integration for agency-agents.
 *
 * Provides a lightweight client that submits agent tasks to a running
 * nexus-orchestrator daemon (https://github.com/el-j/nexus-orchestrator)
 * via its MCP JSON-RPC 2.0 endpoint.
 *
 * The client is entirely optional: it is only instantiated when the user
 * chooses to use nexus-orchestrator as their LLM routing backend.
 *
 * @example
 * ```ts
 * import { getAgent } from 'agency-agents';
 * import { NexusOrchestratorClient, agentTaskInstruction } from 'agency-agents/nexus';
 *
 * const nexus = new NexusOrchestratorClient();
 * const agent = getAgent('frontend-developer')!;
 *
 * const task = await nexus.submitTask({
 *   projectPath: '/my/project',
 *   targetFile:  'src/App.tsx',
 *   instruction: agentTaskInstruction(agent, 'Add dark-mode toggle'),
 * });
 * console.log('Task ID:', task.id, '  Status:', task.status);
 * ```
 */

import type { Agent, Swarm, NexusTask, NexusTaskResult, NexusOrchestratorOptions } from './types.js';

// ---------------------------------------------------------------------------
// Internal MCP JSON-RPC helpers
// ---------------------------------------------------------------------------

interface McpRequest {
  jsonrpc: '2.0';
  method: string;
  params: Record<string, unknown>;
  id: number;
}

interface McpResponse<T = unknown> {
  jsonrpc: '2.0';
  id: number;
  result?: T;
  error?: { code: number; message: string; data?: unknown };
}

async function mcpCall<T>(url: string, toolName: string, args: Record<string, unknown>): Promise<T> {
  const body: McpRequest = {
    jsonrpc: '2.0',
    method: 'tools/call',
    params: { name: toolName, arguments: args },
    id: Date.now(),
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    throw new Error(
      `Nexus Orchestrator HTTP error: ${response.status} ${response.statusText}`,
    );
  }

  const json = (await response.json()) as McpResponse<T>;
  if (json.error) {
    throw new Error(`Nexus Orchestrator MCP error: ${json.error.message}`);
  }
  if (json.result === undefined) {
    throw new Error('Nexus Orchestrator: empty MCP response');
  }
  return json.result;
}

// ---------------------------------------------------------------------------
// NexusOrchestratorClient
// ---------------------------------------------------------------------------

/**
 * Client for interacting with a running nexus-orchestrator daemon.
 *
 * Communicates over JSON-RPC 2.0 via the MCP endpoint (default `:9998/mcp`).
 * All methods are async and throw on network or daemon errors.
 */
export class NexusOrchestratorClient {
  private readonly mcpUrl: string;

  constructor(options: NexusOrchestratorOptions = {}) {
    this.mcpUrl = options.mcpUrl ?? 'http://localhost:9998/mcp';
  }

  /**
   * Submit a code-generation task to the nexus-orchestrator daemon.
   *
   * @param task  Task parameters (`projectPath`, `targetFile`, `instruction`).
   * @returns     The newly created task record with its assigned `id`.
   */
  async submitTask(task: NexusTask): Promise<NexusTaskResult> {
    return mcpCall<NexusTaskResult>(this.mcpUrl, 'submit_task', { ...task });
  }

  /**
   * Poll the status and output of a previously submitted task.
   *
   * @param taskId  The `id` returned by {@link submitTask}.
   */
  async getTask(taskId: string): Promise<NexusTaskResult> {
    return mcpCall<NexusTaskResult>(this.mcpUrl, 'get_task', { id: taskId });
  }

  /**
   * Return all pending / queued tasks visible to the daemon.
   */
  async getQueue(): Promise<NexusTaskResult[]> {
    return mcpCall<NexusTaskResult[]>(this.mcpUrl, 'get_queue', {});
  }

  /**
   * Cancel a queued task by its ID.
   *
   * @param taskId  The `id` of the task to cancel.
   */
  async cancelTask(taskId: string): Promise<void> {
    await mcpCall<unknown>(this.mcpUrl, 'cancel_task', { id: taskId });
  }

  /**
   * Check whether the nexus-orchestrator daemon is reachable.
   *
   * @returns `true` when the daemon responds successfully, `false` otherwise.
   */
  async checkHealth(): Promise<boolean> {
    try {
      await mcpCall<unknown>(this.mcpUrl, 'health', {});
      return true;
    } catch {
      return false;
    }
  }
}

// ---------------------------------------------------------------------------
// Helper utilities
// ---------------------------------------------------------------------------

/**
 * Build the instruction string for a single-agent task.
 *
 * Combines the agent's system prompt with an optional user request so the
 * instruction is fully self-contained when submitted to nexus-orchestrator.
 *
 * @param agent    The resolved agency-agent.
 * @param request  Optional user-facing task description appended after the
 *                 system prompt.
 *
 * @example
 * ```ts
 * const instruction = agentTaskInstruction(frontendAgent, 'Refactor Button to use Tailwind');
 * ```
 */
export function agentTaskInstruction(agent: Agent, request?: string): string {
  const parts: string[] = [agent.systemPrompt];
  if (request) {
    parts.push('', '---', '', request);
  }
  return parts.join('\n');
}

/**
 * Build the instruction string for a swarm orchestration task.
 *
 * Uses the swarm's pre-built `orchestratorPrompt` (which already contains
 * each agent's system prompt) combined with an optional top-level request.
 *
 * @param swarm    The resolved {@link Swarm}.
 * @param request  Optional user-facing task description.
 */
export function swarmTaskInstruction(swarm: Swarm, request?: string): string {
  const parts: string[] = [swarm.orchestratorPrompt];
  if (request) {
    parts.push('', '---', '', request);
  }
  return parts.join('\n');
}
