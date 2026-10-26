# Implement a focused design change

1. Establish the requested target and inspect its source, dependencies, styles, and behavior. Preserve unrelated user changes.
2. For a major redesign, outline the visual direction and affected areas before broad edits. Follow existing authorization; do not repeatedly ask for permission for routine in-scope changes.
3. Make maintainable changes using existing tokens and components. Detect React, Next.js, TypeScript/JavaScript, Tailwind (including version 4), CSS Modules, vanilla CSS, Material UI, or other libraries from the project rather than assuming a stack.
4. Preserve event handlers, state transitions, API calls, routes, authentication, validation and error handling. Extract components only where it simplifies this change. Avoid unrelated refactors.
5. Cover responsive layouts, meaningful interaction states, keyboard/focus behavior and reduced motion where applicable.
6. Run the relevant available lint, type-check, behavior tests and build commands. Use the project's package manager and scripts. Do not claim a command passed if it was unavailable, skipped or failed.
7. If a preview is available, inspect representative mobile, tablet and desktop layouts. Exercise the affected interactions and check for overflow, clipped content, focus regressions and missing states. Screenshots alone do not prove interactive behavior.
8. Correct verified regressions in scope. Summarize changes, files, actual verification and limitations.

## Read-only requests

Audit and suggestion modes do not edit application files, install dependencies, rewrite design tokens, or start an implementation. If saving a report is requested, write only that report. Otherwise respond in chat. Tools that mutate files, even “fix” flags on checks, are inappropriate for read-only inspection.

## Limited environments

Without a running preview, use source inspection and available checks and state that visual behavior remains unverified. Without file tools, offer an implementation sketch rather than pretending to patch the project. Without browsing, base decisions on the project and clearly label gallery links as uninspected starting points.
