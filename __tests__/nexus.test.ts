/// <reference types="vitest" />
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { NexusOrchestratorClient, agentTaskInstruction, swarmTaskInstruction } from '../src/nexus.js';
import { loadAgentsFromDir } from '../src/loader.js';
import { buildSwarm } from '../src/swarm.js';
import type { NexusTaskResult } from '../src/types.js';

const __filename = fileURLToPath(import.meta.url);
const REPO_ROOT = path.resolve(path.dirname(__filename), '..');

// ---------------------------------------------------------------------------
// Fixtures
// ---------------------------------------------------------------------------
function getFixtureAgent() {
  const agents = loadAgentsFromDir(REPO_ROOT);
  return agents[0]!;
}

// ---------------------------------------------------------------------------
// Helper: create a fetch stub that returns a well-formed MCP response
// ---------------------------------------------------------------------------
function mockFetch(result: unknown) {
  return vi.fn().mockResolvedValue({
    ok: true,
    json: async () => ({ jsonrpc: '2.0', id: 1, result }),
  });
}

function mockFetchError(status: number, statusText: string) {
  return vi.fn().mockResolvedValue({ ok: false, status, statusText });
}

function mockFetchMcpError(code: number, message: string) {
  return vi.fn().mockResolvedValue({
    ok: true,
    json: async () => ({ jsonrpc: '2.0', id: 1, error: { code, message } }),
  });
}

// ---------------------------------------------------------------------------
// NexusOrchestratorClient
// ---------------------------------------------------------------------------
describe('NexusOrchestratorClient', () => {
  let originalFetch: typeof globalThis.fetch;

  beforeEach(() => {
    originalFetch = globalThis.fetch;
  });

  afterEach(() => {
    globalThis.fetch = originalFetch;
    vi.restoreAllMocks();
  });

  it('uses default MCP URL when no options are given', async () => {
    const taskResult: NexusTaskResult = { id: 'abc', status: 'queued' };
    globalThis.fetch = mockFetch(taskResult);

    const client = new NexusOrchestratorClient();
    await client.submitTask({ projectPath: '/p', targetFile: 'f.ts', instruction: 'do it' });

    expect(globalThis.fetch).toHaveBeenCalledWith(
      'http://localhost:9998/mcp',
      expect.objectContaining({ method: 'POST' }),
    );
  });

  it('accepts a custom MCP URL', async () => {
    const taskResult: NexusTaskResult = { id: 'abc', status: 'queued' };
    globalThis.fetch = mockFetch(taskResult);

    const client = new NexusOrchestratorClient({ mcpUrl: 'http://myhost:9998/mcp' });
    await client.submitTask({ projectPath: '/p', targetFile: 'f.ts', instruction: 'do it' });

    expect(globalThis.fetch).toHaveBeenCalledWith(
      'http://myhost:9998/mcp',
      expect.anything(),
    );
  });

  // ── submitTask ─────────────────────────────────────────────────────────

  it('submitTask returns the task result on success', async () => {
    const taskResult: NexusTaskResult = { id: 'task-1', status: 'queued' };
    globalThis.fetch = mockFetch(taskResult);

    const client = new NexusOrchestratorClient();
    const result = await client.submitTask({
      projectPath: '/project',
      targetFile: 'src/main.ts',
      instruction: 'Refactor this file',
    });

    expect(result.id).toBe('task-1');
    expect(result.status).toBe('queued');
  });

  it('submitTask sends the correct MCP tool name', async () => {
    globalThis.fetch = mockFetch({ id: 'x', status: 'queued' });
    const client = new NexusOrchestratorClient();
    await client.submitTask({ projectPath: '/p', targetFile: 'f.ts', instruction: 'test' });

    const body = JSON.parse((globalThis.fetch as ReturnType<typeof vi.fn>).mock.calls[0][1].body as string);
    expect(body.params.name).toBe('submit_task');
  });

  it('submitTask throws on HTTP error', async () => {
    globalThis.fetch = mockFetchError(500, 'Internal Server Error');
    const client = new NexusOrchestratorClient();

    await expect(
      client.submitTask({ projectPath: '/p', targetFile: 'f.ts', instruction: 'test' }),
    ).rejects.toThrow('500');
  });

  it('submitTask throws on MCP error response', async () => {
    globalThis.fetch = mockFetchMcpError(-32600, 'Invalid Request');
    const client = new NexusOrchestratorClient();

    await expect(
      client.submitTask({ projectPath: '/p', targetFile: 'f.ts', instruction: 'test' }),
    ).rejects.toThrow('Invalid Request');
  });

  // ── getTask ────────────────────────────────────────────────────────────

  it('getTask sends the correct tool and task ID', async () => {
    const taskResult: NexusTaskResult = { id: 'task-99', status: 'completed', output: 'Done!' };
    globalThis.fetch = mockFetch(taskResult);

    const client = new NexusOrchestratorClient();
    const result = await client.getTask('task-99');

    expect(result.id).toBe('task-99');
    expect(result.output).toBe('Done!');

    const body = JSON.parse((globalThis.fetch as ReturnType<typeof vi.fn>).mock.calls[0][1].body as string);
    expect(body.params.name).toBe('get_task');
    expect(body.params.arguments).toEqual({ id: 'task-99' });
  });

  // ── getQueue ───────────────────────────────────────────────────────────

  it('getQueue returns an array of tasks', async () => {
    const queue: NexusTaskResult[] = [
      { id: 'a', status: 'queued' },
      { id: 'b', status: 'in_progress' },
    ];
    globalThis.fetch = mockFetch(queue);

    const client = new NexusOrchestratorClient();
    const result = await client.getQueue();

    expect(result).toHaveLength(2);
    expect(result[0]?.id).toBe('a');
  });

  // ── cancelTask ─────────────────────────────────────────────────────────

  it('cancelTask sends the correct tool and task ID', async () => {
    globalThis.fetch = mockFetch(null);
    const client = new NexusOrchestratorClient();
    await client.cancelTask('task-42');

    const body = JSON.parse((globalThis.fetch as ReturnType<typeof vi.fn>).mock.calls[0][1].body as string);
    expect(body.params.name).toBe('cancel_task');
    expect(body.params.arguments).toEqual({ id: 'task-42' });
  });

  // ── checkHealth ────────────────────────────────────────────────────────

  it('checkHealth returns true when daemon responds', async () => {
    globalThis.fetch = mockFetch({ status: 'ok' });
    const client = new NexusOrchestratorClient();
    expect(await client.checkHealth()).toBe(true);
  });

  it('checkHealth returns false when fetch throws', async () => {
    globalThis.fetch = vi.fn().mockRejectedValue(new Error('ECONNREFUSED'));
    const client = new NexusOrchestratorClient();
    expect(await client.checkHealth()).toBe(false);
  });

  it('checkHealth returns false on HTTP error', async () => {
    globalThis.fetch = mockFetchError(503, 'Service Unavailable');
    const client = new NexusOrchestratorClient();
    expect(await client.checkHealth()).toBe(false);
  });
});

// ---------------------------------------------------------------------------
// agentTaskInstruction
// ---------------------------------------------------------------------------
describe('agentTaskInstruction', () => {
  it('returns the agent system prompt when no request is given', () => {
    const agent = getFixtureAgent();
    const instruction = agentTaskInstruction(agent);
    expect(instruction).toBe(agent.systemPrompt);
  });

  it('appends the request after a separator when provided', () => {
    const agent = getFixtureAgent();
    const request = 'Add dark-mode support';
    const instruction = agentTaskInstruction(agent, request);
    expect(instruction).toContain(agent.systemPrompt);
    expect(instruction).toContain('---');
    expect(instruction).toContain(request);
    // request must come after the system prompt
    expect(instruction.indexOf(request)).toBeGreaterThan(instruction.indexOf(agent.systemPrompt));
  });

  it('does not append a separator when request is an empty string', () => {
    const agent = getFixtureAgent();
    const instruction = agentTaskInstruction(agent, '');
    expect(instruction).toBe(agent.systemPrompt);
  });
});

// ---------------------------------------------------------------------------
// swarmTaskInstruction
// ---------------------------------------------------------------------------
describe('swarmTaskInstruction', () => {
  it('returns the swarm orchestratorPrompt when no request is given', () => {
    const agents = loadAgentsFromDir(REPO_ROOT).slice(0, 2);
    const swarm = buildSwarm(agents);
    const instruction = swarmTaskInstruction(swarm);
    expect(instruction).toBe(swarm.orchestratorPrompt);
  });

  it('appends the request after a separator when provided', () => {
    const agents = loadAgentsFromDir(REPO_ROOT).slice(0, 2);
    const swarm = buildSwarm(agents, { name: 'Test Swarm' });
    const request = 'Ship the MVP by Friday';
    const instruction = swarmTaskInstruction(swarm, request);
    expect(instruction).toContain(swarm.orchestratorPrompt);
    expect(instruction).toContain('---');
    expect(instruction).toContain(request);
  });
});
