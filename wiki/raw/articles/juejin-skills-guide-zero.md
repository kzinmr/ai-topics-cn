# Skill 入门指南：从零开始打造你的智能编程助手

**Source:** 掘金
**Date:** 2026-04-23
**URL:** https://juejin.cn/post/7631473695154192410
**Categories:** [AI Skills, SKILL.md, 智能编程, Trae IDE]

## Summary
Guide on creating custom AI coding Skills. Skills are reusable, customizable intelligence units packaged as SKILL.md files. Connect IDE, LLM, and development tools for specific programming problems.

## Core Features
1. Modular design (single responsibility)
2. Standardized interfaces (cross-agent interoperability)
3. Context awareness (tech stack, code style, history)
4. On-demand loading (no redundant resource usage)
5. Customizable (personal/team habit adaptation)

## Directory Structure
```
my-skill/
├── SKILL.md        # Core config file
├── examples/       # Input/output examples (optional)
└── README.md       # Documentation (optional)
```

## Tool: skills.sh
- Install: `curl -fsSL https://skills.sh/install.sh | bash`
- Search: `skills search react`
- Install: `skills install trae-ai/react-component-generator`
- Publish: `skills publish`

## IDE Config (Trae IDE)
- Settings → AI Models: fill OpenAI/Claude API key
- Settings → Rules & Skills → Skill Repositories: paste GitHub repo
- Local: `.trae/skills/` folder in project root
- Trigger: `@` symbol or direct instruction
