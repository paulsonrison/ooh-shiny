# Validation record

Release: 0.1.0. Checked on 2026-10-26. These results distinguish package checks from behavioral and live-host evidence.

## Automated checks passed

- `python scripts/validate.py`: portable manifest against the official Agent Plugins 1.0.0 JSON Schema; host manifest identity/version agreement; marketplace entries; skill/UI metadata; local reference links; ZIP integrity and layouts; identical shared skill contents; exclusion of unlisted private files.
- OpenAI's bundled `skill-creator/scripts/quick_validate.py`: skill valid.
- Both focused archives generated successfully with SHA-256 checksums.
- Windows validation used Python 3.12, PyYAML 6.0.3 and jsonschema 4.26.0. The bundled validator required UTF-8 mode; the restricted environment required a writable workspace temporary directory.
- The schema snapshot in `scripts/plugin.schema.json` was retrieved from https://agent-plugins.org/schemas/1.0.0/plugin.schema.json on 2026-10-26. It is used for offline validation; its extension namespace does not validate OpenAI-specific presentation fields.

## Personal Codex installation verified

`codex plugin add ooh-shiny@ooh-shiny-personal --json` installed version 0.1.0 through the native installer. `codex plugin list --json` reported `installed: true` and `enabled: true`. One personal marketplace entry points to the local package, and there is no separate standalone skill installation. The host's managed plugin cache is an expected installation artifact, not a competing standalone copy.

Desktop skill-selector refresh and end-to-end invocation in a new desktop conversation have not been verified; restart the app if the skill is not yet visible. Claude Code, Cursor and Copilot instructions were checked against vendor documentation; their live runtimes were not tested.

## Independent behavioral evaluation

An independent agent used the skill with a disposable dashboard fixture. Audit and navbar/hero/theme suggestions left application hashes unchanged. A subsequent CSS-only CTA/menu/card improvement preserved the component source hash and callback behavior in a minimal React API shim. Static checks covered reduced-motion overrides, bounded transitions and focus styling. Backend scope reasoning and no-browser research honesty were also exercised.

This was not a real React renderer or browser test. Responsive layout, rendered contrast, keyboard focus movement, touch behavior, live gallery research quality, and host automatic skill selection remain unverified. The backend scenario tested scope reasoning rather than the host's routing algorithm. See `evals/scenarios.md` for repeatable acceptance scenarios.

The independent review reproduced an archive bug: arbitrary files added under the skill could enter both archives. Packaging now uses an explicit file allowlist; a regression check inserts an unrelated private note in a disposable copy and confirms exclusion from both ZIPs.

## Design-source availability

All seven landing pages were retrieved using web tools during release preparation. This verifies entry-point availability at that time, not individual examples, licensing, or animation behavior. Supahero identifies itself as part of Screensdesign; Scrolltide advertises paid access; 3Dicons includes both free and premium assets. The skill therefore rechecks actual sources during use and supports unavailable browsing.
