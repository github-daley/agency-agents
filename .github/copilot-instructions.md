# The Agency repository instructions

## Build, test, and lint commands

Run commands from the repository root.

```bash
# Validate all lint-covered agent files
./scripts/lint-agents.sh

# Validate a single agent file
./scripts/lint-agents.sh engineering/engineering-frontend-developer.md

# Regenerate all converted integration outputs
./scripts/convert.sh

# Regenerate one integration target only
./scripts/convert.sh --tool cursor

# Install generated outputs for one tool
./scripts/install.sh --tool copilot
```

`lint-agents.sh` is the main automated validation entry point. `convert.sh` generates tool-specific outputs under `integrations/`, and `install.sh` copies those generated outputs into local tool configuration locations.

## High-level architecture

This repository is a source catalog of agent definitions, not a conventional application. The source of truth is the Markdown agent files in the category directories such as `engineering/`, `marketing/`, `testing/`, and related top-level domains.

Each agent file has YAML frontmatter plus a structured Markdown body. The repository workflow is:

1. Author or update an agent Markdown file in a category directory.
2. Run `./scripts/lint-agents.sh` to validate frontmatter and basic structure.
3. Run `./scripts/convert.sh` to transform source agents into tool-specific formats under `integrations/`.
4. Run `./scripts/install.sh` to copy those generated files into the target tool's local config directories.

The core pipeline is split across three scripts:

- `scripts/lint-agents.sh` validates required frontmatter fields and checks for a few recommended section patterns.
- `scripts/convert.sh` parses the category Markdown files, extracts frontmatter, strips the body, and emits tool-specific outputs for Cursor, Copilot, Gemini CLI, Antigravity, Aider, Windsurf, OpenCode, OpenClaw, and Qwen.
- `scripts/install.sh` reads from `integrations/` and installs into user-level or project-level directories depending on the target tool.

One non-obvious detail: OpenClaw output is derived by splitting agent bodies into persona-oriented sections and operations-oriented sections. The section names you use in source Markdown affect how `convert.sh` distributes content into `SOUL.md`, `AGENTS.md`, and `IDENTITY.md`.

## Key conventions

Agent files are expected to follow the structure described in `CONTRIBUTING.md`: frontmatter first, then a body that separates persona from operations. Keep identity, communication style, and critical rules clearly labeled, then keep mission, deliverables, workflow, success metrics, and advanced capabilities in their own sections.

At minimum, frontmatter must include `name`, `description`, and `color`, because that is what `scripts/lint-agents.sh` enforces. In practice, `emoji` and `vibe` are also important because `scripts/convert.sh` uses them when generating OpenClaw `IDENTITY.md`, and they are part of the documented authoring template.

Use clear `##` section headers that preserve the repository's existing vocabulary. In particular, headers containing terms like `Identity`, `Communication Style`, and `Critical Rules` are significant because `convert.sh` uses those keywords to classify content for OpenClaw output. Everything else is treated as operational content.

This repository favors strong, specialized agent voices over generic assistant prose. Follow the patterns in the existing agents and `CONTRIBUTING.md`: narrow scope, a memorable persona, concrete deliverables, measurable success metrics, and step-by-step workflows. Representative examples called out in the docs are `engineering/engineering-frontend-developer.md`, `marketing/marketing-reddit-community-builder.md`, and `design/design-whimsy-injector.md`.

If an agent depends on external services, declare them in frontmatter under `services:` with `name`, `url`, and `tier`. The contribution guidelines expect these dependencies only when they are essential to the agent and prefer tools with free tiers.

Avoid editing generated integration outputs as if they were source files. The authored Markdown files in the category directories are the canonical inputs; regenerate derived outputs with `./scripts/convert.sh`.

Keep PR-scale changes narrow unless the repo already documents otherwise. `CONTRIBUTING.md` explicitly treats a new or improved single agent Markdown file as the normal contribution unit, while broader tooling or multi-file structural changes should be approached more carefully.

Be aware that validation coverage is not perfectly symmetrical across categories. `scripts/convert.sh` includes `academic/` and `sales/`, but `scripts/lint-agents.sh` currently does not scan every converted category. When editing agents in categories outside the linter's scan list, compare them closely against the template and existing high-quality agents.
