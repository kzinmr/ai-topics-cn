# 别再裸用 Claude Code 了！32个亲测Skills + 8个MCP

**Source:** 掘金
**Date:** 2026-04-23
**URL:** https://juejin.cn/post/7620060655607857178
**Categories:** [Claude Code, Skills, MCP, 开发效率]

## Summary
Comprehensive guide for enhancing Claude Code with 32 Skills and 8 MCP servers. Skills = workflow prompts that make Claude "smarter"; MCP servers = local tools that make Claude "capable." Installation via `npx skills add <repo> -y -g` for Skills, and `~/.claude/mcp.json` for MCP servers.

## Key Skills Categories
- **Frontend:** frontend-design, web-artifacts-builder, vercel-react-best-practices, shadcn/ui
- **Documentation:** technical-writer, docx/pptx/xlsx/pdf
- **Architecture:** planning-with-files, requesting-code-review, architecture-patterns
- **Memory:** memory-intake, memory-audit
- **Debugging:** systematic-debugging, brainstorming

## Key MCP Servers
- Neural Memory (long-term structured memory)
- Filesystem (local file access)
- Playwright (browser automation/E2E testing)
- Figma (design spec integration)

## Pitfalls
- Don't install >20 skills simultaneously (increases context load)
- Always use `-g` flag for global installation
- Restart Claude Code after installing skills
- Never grant filesystem MCP access to system root directory
