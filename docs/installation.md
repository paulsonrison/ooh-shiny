# Installation and compatibility

One canonical skill lives in `skills/ooh-shiny/`. Both plugin manifests discover that same folder. Do not activate a standalone copy and a plugin copy in the same host.

## Personal Codex plugin

The simplest online installation is `codex plugin marketplace add paulsonrison/ooh-shiny` followed by `codex plugin add ooh-shiny@ooh-shiny-marketplace`. For a personal local package instead, follow these steps:

1. Copy the package to `~/.codex/plugins/ooh-shiny/`, including hidden manifest directories.
2. Merge this entry into `~/.agents/plugins/marketplace.json`, preserving existing marketplace metadata and plugin entries. If the file does not exist, use top-level `name: ooh-shiny-personal` and a `plugins` array.

```json
{
  "name": "ooh-shiny",
  "source": {"source": "local", "path": "./.codex/plugins/ooh-shiny"},
  "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
  "category": "Productivity"
}
```

The personal marketplace resolves this path from the home directory. For a different installation directory, use a valid path within that marketplace root. Do not overwrite an existing plugin with the same identifier without reviewing it.

3. Run `codex plugin add ooh-shiny@ooh-shiny-personal` (substitute your existing marketplace name if it already had one), or select the available plugin in the plugin UI. Inspect `codex plugin --help` for older CLI versions. Restart the desktop app to reload discovery if needed.
4. Invoke the discovered skill as `$ooh-shiny`, or select it by name in the skill selector. A plugin host may namespace the visible skill name.

The repository's `.agents/plugins/marketplace.json` offers a repository-local marketplace pointing at its root. It is not a global installation by itself.

Alternatively, copy only `skills/ooh-shiny` to `~/.agents/skills/ooh-shiny` for a standalone personal skill. Choose this instead of installing the plugin, not in addition.

## Claude Code

Register and install the repository marketplace using the README commands. For a local preview, launch `claude --plugin-dir /absolute/path/to/ooh-shiny`. Validate with `claude plugin validate /absolute/path/to/ooh-shiny` when the CLI is installed. The plugin command is `/ooh-shiny:ooh-shiny`; a standalone skill is `/ooh-shiny`.

## Cursor

Copy the entire skill folder to `.cursor/skills/ooh-shiny/` in the target repository, or `~/.cursor/skills/ooh-shiny/` for local personal use. Cursor also documents `.agents/skills` support. Use `/` in Agent chat to find the skill. Personal local installation does not imply installation in cloud or remote environments.

## GitHub Copilot

Copy the entire skill folder to `.github/skills/ooh-shiny/` in the repository for project use. For local surfaces supporting personal skills, use `~/.copilot/skills/ooh-shiny/`. Availability depends on the Copilot surface and version. Commit project skills when a cloud agent needs them; it cannot assume access to your home directory.

## Other AI tools

Use the host's documented Agent Skills directory if it supports the standard. Otherwise attach the skill and relevant references as instructions. Browsing-only assistants can research and suggest; code editing and verification require development tools. No universal automatic installation is claimed.

## Compatibility evidence

Documentation checked on 2026-10-26; documentation verification does not equal live host testing. See `validation.md` for actual checks.

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Claude Code manifests](https://code.claude.com/docs/en/plugins-reference)
- [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Cursor skills and supported directories](https://cursor.com/docs/skills)
- [Copilot skills and supported surfaces](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)
- [Agent Skills specification](https://agentskills.io/specification)
