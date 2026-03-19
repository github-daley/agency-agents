# 🎭 The Agency：AI 专家智能体集合

[English](README.md) | 简体中文

> 一个放进仓库就能直接用起来的 AI 专家团队。从前端开发、代码审查到增长、运营、测试、项目管理，这个仓库提供了大量可复用的专业智能体定义。

---

## 项目简介

**The Agency** 是一个以 Markdown 文件组织的智能体仓库。每个 agent 都不只是一个简短 prompt，而是包含：

- 明确的角色定位与人格风格
- 核心任务与工作流程
- 可交付物模板
- 质量标准与成功指标

你可以把它理解成一个“可移植的 AI 专家团队模板库”。

这个仓库当前尤其适合：

- 想快速给 Codex、Claude Code、Cursor、Aider 等工具加一批专业 agent 的团队
- 想把通用 AI 编程工具改造成“按岗位分工”的工作流
- 想把 prompt 资产沉淀到仓库里并持续维护的人

---

## 快速开始

### 方式 1：直接当作 Agent 素材库使用

每个 agent 都是一个独立的 `.md` 文件，分布在不同业务目录下，比如：

- [engineering](engineering)
- [design](design)
- [marketing](marketing)
- [testing](testing)
- [specialized](specialized)

你可以直接阅读、复制、改写这些 agent 定义。

### 方式 2：安装到 Codex

这个仓库现在已经支持 `Codex` 集成。

```bash
cd /path/to/agency-agents
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```

安装完成后会把技能写入：

```bash
~/.codex/skills/
```

注意：

- Codex 版 skill 现在支持**中文显示名称**
- skill 正文仍保留英文原始指令，方便保持兼容
- 安装后需要**重启 Codex**

在 Codex 中可以这样调用：

```text
Use the "前端开发工程师" skill to review this component.
```

```text
Use the "现实检验官" skill and tell me if this feature is production-ready.
```

Codex 的详细说明见：

- [integrations/codex/README.md](integrations/codex/README.md)

### 方式 3：安装到其他工具

仓库还支持多种 agentic coding 工具：

- Claude Code
- GitHub Copilot
- Codex
- Cursor
- Aider
- Windsurf
- Gemini CLI
- Antigravity
- OpenCode
- OpenClaw
- Qwen Code

通用流程是：

```bash
./scripts/convert.sh
./scripts/install.sh
```

或指定工具：

```bash
./scripts/install.sh --tool cursor
./scripts/install.sh --tool codex
./scripts/install.sh --tool aider
```

完整集成文档见：

- [integrations/README.md](integrations/README.md)

---

## 仓库结构

### Agent 目录

这些目录存放原始 agent 定义：

- [academic](academic)：学术与世界观构建
- [design](design)：设计与视觉体验
- [engineering](engineering)：软件工程与架构
- [game-development](game-development)：游戏开发
- [marketing](marketing)：增长与内容营销
- [paid-media](paid-media)：广告投放
- [sales](sales)：销售流程
- [product](product)：产品管理
- [project-management](project-management)：项目管理
- [testing](testing)：测试与质量验证
- [support](support)：支持与运营
- [spatial-computing](spatial-computing)：空间计算
- [specialized](specialized)：特殊领域专家

### 脚本目录

- [scripts/convert.sh](scripts/convert.sh)：把原始 agent 转换成各工具格式
- [scripts/install.sh](scripts/install.sh)：安装到本地工具目录
- [scripts/lint-agents.sh](scripts/lint-agents.sh)：校验 agent 文件

### 集成目录

- [integrations](integrations)：各工具的安装与格式说明

---

## 常用命令

### 生成所有工具的集成文件

```bash
./scripts/convert.sh
```

### 只生成 Codex 版本

```bash
./scripts/convert.sh --tool codex
```

### 自动检测并安装到本机已有工具

```bash
./scripts/install.sh
```

### 只安装 Codex

```bash
./scripts/install.sh --tool codex
```

### 并行执行，提高速度

```bash
./scripts/convert.sh --parallel
./scripts/install.sh --no-interactive --parallel
```

---

## 推荐使用方式

如果你主要使用 `Codex`，推荐这样组织工作流：

1. 从 [engineering](engineering) 和 [testing](testing) 目录开始
2. 先安装 `codex` 版本 skills
3. 用中文显示名直接调用 skill
4. 按需要逐步补充营销、产品、项目管理等 agent

例如：

```text
Use the "后端架构师" skill to design this API.
```

```text
Use the "代码审查专家" skill to review this change.
```

```text
Use the "现实检验官" skill to verify whether this feature is really ready.
```

---

## 说明与范围

这份中文 README 主要解决“快速上手”和“安装使用”问题。

如果你需要：

- 完整 agent 名录
- 全量英文说明
- 更细的各工具集成细节
- 社区翻译信息

请继续参考英文主文档：

- [README.md](README.md)

---

## 贡献

如果你要新增 agent、补充集成、修正 prompt，可以先看：

- [CONTRIBUTING.md](CONTRIBUTING.md)

如果你要继续完善中文文档，一个比较自然的下一步是：

- 增补常用 agent 的中英文对照表
- 给 `integrations/` 下的各工具 README 增加中文版
- 按业务目录补充中文导览页
