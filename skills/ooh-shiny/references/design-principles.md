# Visual and usability decisions

## Audit and suggest

Tie findings to evidence: component/file, screenshot region, viewport, or observable interaction. Prioritize blocked tasks and confusing interactions before cosmetic polish. Separate confirmed defects from preferences and hypotheses.

Assess hierarchy, readability, spacing, typography, color roles, navigation, component consistency, responsive behavior, and interaction states. A suggestion should connect an observed issue to a concrete change and expected benefit; explain effort and meaningful risks. Present distinct directions only when the user would benefit from choosing between them.

## Design within the product

Follow existing tokens unless the user requested a redesign. When new tokens are needed, define reusable semantic colors, type sizes, spacing, radii, shadows, and motion values in the project's existing theme system. Avoid scattered one-off values. Preserve the brand's recognizable character.

Use real content lengths and realistic empty, loading, error, and success states. Make the primary action obvious. Avoid decorative 3D, gradients, glass, or parallax unless they reinforce the product's purpose.

## Responsive and accessible

Use semantic elements and accessible names, visible focus, keyboard interaction, and readable contrast. Aim for WCAG 2.2 AA where applicable, including text and control contrast and target sizing; do not assert compliance without an appropriate audit. Prefer established accessible components over hand-built complex widgets.

Check small mobile, tablet, and desktop widths, plus long labels and zoom/reflow when relevant. Prevent horizontal overflow and clipped popovers. Keep navigation and critical actions accessible when layouts collapse. Do not convey state through color alone or hide essential controls behind hover-only interactions.

Use modest asset sizes and stable media dimensions. Preserve content hierarchy and avoid layout shifts, especially around loading content and font swaps.
