# OMEGA Memory Integration

> Give any agent persistent, semantically searchable memory across sessions using [OMEGA](https://github.com/omega-memory/omega-memory), an MCP memory server.

## What It Does

OMEGA is an MCP memory server that provides structured, persistent memory for AI coding agents. Unlike simple key-value memory stores, OMEGA offers:

- **Semantic search**: Query memories by meaning, not just keywords. OMEGA uses local embeddings (ONNX, no API calls) to find relevant context even when the wording differs.
- **Typed memories**: Store decisions, lessons learned, error patterns, user preferences, constraints, and session summaries as distinct types with different retention behaviors.
- **Memory decay and consolidation**: Old, low-value memories fade over time. Important memories are reinforced through access. This keeps the memory store relevant without manual pruning.
- **Contradiction detection**: When you store a memory that conflicts with an existing one, OMEGA flags the contradiction so agents don't act on stale information.
- **Cross-session continuity**: Agents pick up exactly where they left off. Checkpoint a task mid-session, resume it in the next one.
- **Multi-agent coordination**: Memories are scoped by agent type, entity, and project. Multiple agents can share a memory store without stepping on each other.

## Setup

### Requirements

- Python 3.11+
- An MCP-compatible client (Claude Code, Cursor, etc.)

### Install

```bash
pip install omega-memory
```

Or run the setup script:

```bash
./integrations/omega-memory/setup.sh
```

### Configure Your MCP Client

Add OMEGA to your MCP client config. For Claude Code (`~/.claude.json`):

```json
{
  "mcpServers": {
    "omega": {
      "command": "python3.11",
      "args": ["-m", "omega.server.mcp_server"]
    }
  }
}
```

For other clients, adapt the command/args to your MCP config format.

## Available Tools

OMEGA exposes these MCP tools:

| Tool | Description |
|------|-------------|
| `omega_store` | Store a memory with type, metadata, priority, and entity/project scoping |
| `omega_query` | Search memories by semantic similarity, exact phrase, timeline, or browse by type |
| `omega_welcome` | Session greeting with context briefing from recent memories |
| `omega_protocol` | Returns the agent's operating protocol and instructions |
| `omega_profile` | Load or update an entity/project profile |
| `omega_checkpoint` | Save current task state for later resumption |
| `omega_resume_task` | Resume a previously checkpointed task |
| `omega_memory` | Direct memory operations (read, update, delete) |
| `omega_remind` | Set and retrieve reminders |
| `omega_maintain` | Run maintenance operations (decay, consolidation, cleanup) |
| `omega_stats` | Memory store statistics and health metrics |
| `omega_reflect` | Analyze patterns across stored memories |

## How to Add OMEGA Memory to Any Agent

Add a **Memory Integration** section to an agent's prompt. See [memory-section-template.md](memory-section-template.md) for a ready-to-use template.

The key differences from generic MCP memory instructions:

1. **Use typed storage**: Instead of generic `remember`, use `omega_store` with `event_type` to categorize what you're storing (decision, lesson_learned, error_pattern, user_preference).
2. **Use semantic search**: `omega_query` with mode `semantic` finds relevant memories even when the exact wording differs from what was stored.
3. **Use checkpoints**: `omega_checkpoint` and `omega_resume_task` handle mid-session saves and cross-session continuity without manual bookkeeping.
4. **Session start protocol**: Call `omega_welcome()` at session start to get a context briefing, then `omega_protocol()` for operating instructions.

## How It Enhances Agency Agents

When agents in The Agency use OMEGA:

- **Session continuity**: An agent resumes work without re-explaining context. The Backend Architect remembers the database schema it designed last week.
- **Cross-agent handoffs**: When the Backend Architect hands off to the Frontend Developer, the API spec is already in memory, tagged and searchable.
- **Learning from mistakes**: Error patterns and lessons learned persist. An agent that hit a race condition once will remember the fix next time.
- **Decision tracking**: Architecture decisions, their reasoning, and their outcomes are stored and searchable. No more re-litigating settled questions.

## Example: Memory-Enhanced Workflow

```
Session 1 (Backend Architect):
  -> omega_welcome() — gets context from prior sessions
  -> Designs API schema
  -> omega_store("API uses REST with JWT auth, rate limited at 100 req/min",
                  event_type="decision", metadata={"project": "acme"})
  -> omega_checkpoint("api-design-phase-1")

Session 2 (Frontend Developer):
  -> omega_welcome() — sees the Backend Architect's API decisions
  -> omega_query("API authentication approach", mode="semantic")
  -> Builds the frontend against the documented API contract
```

## Links

- **GitHub**: [omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)
- **PyPI**: [omega-memory](https://pypi.org/project/omega-memory/)
- **Documentation**: See the GitHub README for full documentation
