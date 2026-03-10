/**
 * agency-agents — Public API
 *
 * @example
 * ```ts
 * import { getAgent, listAgents, buildSwarm } from 'agency-agents';
 *
 * const agent = getAgent('frontend-developer');
 * const swarm = buildSwarm([agent!], { mission: 'Build a React dashboard' });
 * console.log(swarm.orchestratorPrompt);
 * ```
 */

// Types
export type {
  Agent,
  AgentCategory,
  AgentFrontmatter,
  Swarm,
  SwarmOptions,
  NexusTask,
  NexusTaskResult,
  NexusTaskStatus,
  NexusOrchestratorOptions,
} from './types.js';

// Agent loading
export { loadAgents, getAgent, listAgents, listCategories } from './registry.js';

// Swarm orchestration
export { buildSwarm } from './swarm.js';

// Nexus Orchestrator integration (optional)
export { NexusOrchestratorClient, agentTaskInstruction, swarmTaskInstruction } from './nexus.js';

// Lower-level utilities (for advanced consumers)
export {
  loadAgentsFromDir,
  loadAgentFile,
  collectMarkdownFiles,
  slugify,
  AGENT_CATEGORIES,
} from './loader.js';
