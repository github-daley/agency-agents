# Codex Integration

Packages Agency agents as Codex custom skills. Each agent becomes a folder-based
skill stored as `SKILL.md` in `~/.codex/skills/<slug>/`.
Generated Codex skills use Chinese-localized `name` and `description` fields
for display, while preserving the original English skill body for behavior.

## Install

```bash
# Generate the Codex skill files first
./scripts/convert.sh --tool codex

# Then install them into ~/.codex/skills/
./scripts/install.sh --tool codex
```

Restart Codex after installing new skills so it picks them up.

## Activate a Skill

In Codex, reference a skill naturally in your prompt:

```
Use the "前端开发工程师" skill to review this React component.
```

```
Use the "现实检验官" skill and tell me if this feature is production-ready.
```

Codex can also auto-trigger a skill when your request clearly matches the
skill's description.

## Skill Structure

```
~/.codex/skills/
  frontend-developer/
    SKILL.md
  backend-architect/
    SKILL.md
  reality-checker/
    SKILL.md
  ...
```

Each generated `SKILL.md` contains minimal frontmatter plus the original
Agency agent instructions:

```yaml
---
name: "前端开发工程师"
description: "The Agency 中文技能：前端开发工程师。原始角色名：Frontend Developer。详细指令保留在英文正文中。"
---
```

## Regenerate

```bash
./scripts/convert.sh --tool codex
```
