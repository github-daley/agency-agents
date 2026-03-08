# Agency Agents - Claude Code Instructions

This is a collection of 61+ specialized AI agent prompts organized into 9 divisions. It is a documentation-only project (Markdown + Bash scripts, zero external dependencies).

## Project Structure

```
design/              # 7 design agents
engineering/         # 8 engineering agents
marketing/           # 11 marketing agents
product/             # 3 product agents
project-management/  # 5 project management agents
testing/             # 8 testing agents
support/             # 6 support agents
spatial-computing/   # 6 spatial computing agents
specialized/         # 7 specialized agents
strategy/            # Strategy guides, playbooks, runbooks
examples/            # Example workflows
integrations/        # Tool-specific integration configs (7 platforms)
scripts/             # convert.sh, install.sh, lint-agents.sh
```

## Lint / Validate

Run the linter before committing any agent file changes:

```bash
bash scripts/lint-agents.sh
```

To lint specific files only:

```bash
bash scripts/lint-agents.sh path/to/agent.md
```

The linter checks:
- YAML frontmatter exists with required fields: `name`, `description`, `color`
- Recommended sections: Identity, Core Mission, Critical Rules
- Minimum content length (50+ words in body)

Errors (missing frontmatter fields) cause a non-zero exit. Warnings (missing recommended sections, short body) are reported but do not fail.

## Agent File Format

Every agent markdown file must follow this structure:

```markdown
---
name: Agent Name
description: One-line description
color: colorname or "#hexcode"
---

# Agent Name

## Identity / Your Identity & Memory
## Core Mission / Your Core Mission
## Critical Rules / Critical Rules You Must Follow
## Technical Deliverables
## Workflow Process
## Communication Style
## Success Metrics
```

The YAML frontmatter (`name`, `description`, `color`) is required. The sections Identity, Core Mission, and Critical Rules are strongly recommended.

## Agent Divisions

Agents are organized into these directories (one `.md` file per agent):
- `design/` - UI/UX, brand, visual design specialists
- `engineering/` - Frontend, backend, AI, DevOps, security, mobile specialists
- `marketing/` - Growth, content, social media platform specialists
- `product/` - Sprint planning, research, feedback synthesis
- `project-management/` - Production, coordination, operations
- `testing/` - QA, API testing, performance, accessibility
- `support/` - Customer support, analytics, finance, legal, infrastructure
- `spatial-computing/` - AR/VR/XR, visionOS, macOS spatial
- `specialized/` - Orchestration, data analytics, LSP, identity/trust

## Integration / Conversion

The `scripts/convert.sh` script converts agents to formats for other tools (Cursor, Aider, Windsurf, Gemini, OpenCode). Claude Code uses the native `.md` format directly — no conversion needed.

Generated integration files are gitignored. Only source agent files and integration READMEs are committed.

## Contributing

- Follow the agent template structure in CONTRIBUTING.md
- Test agents in real scenarios before submitting
- Run `bash scripts/lint-agents.sh` and fix any errors before committing
- PR titles: "Add [Agent Name] - [Category]"
