# Purposeful motion

Identify the purpose first: communicate state, connect related elements, acknowledge input, or guide attention. If movement adds no information or usability benefit, omit it.

Prefer the existing animation solution and native CSS for simple transitions. Consider Motion for React or GSAP only when the requested interaction warrants it and the project's actual versions are compatible. Do not install a library by default.

Use short, consistent timings derived from existing tokens. As starting points, feedback often needs roughly 100–180 ms and overlays roughly 180–280 ms; tune to the interaction rather than treating these as mandatory values. Prefer transform and opacity where suitable, and avoid transition: all.

## Interaction integrity

- Buttons: distinct focus, hover, pressed, disabled and loading feedback; prevent accidental double submission using existing behavior.
- Menus, dialogs and drawers: preserve keyboard navigation, focus management, dismissal, and accessible state. An exiting overlay must not leave invisible interactive elements trapping focus.
- Tabs and accordions: communicate selection/expansion semantically; do not delay content access until animation completion.
- Scroll reveals: content remains available if motion, JavaScript, or observers are disabled. Avoid scroll hijacking and excessive parallax.
- Route transitions: respect the router's lifecycle, focus/scroll restoration, and user navigation. Do not delay routing or data loading for spectacle.

## Reduced motion and performance

Honor prefers-reduced-motion using CSS media queries or the framework's supported mechanism. Remove nonessential travel, parallax, looping and large scaling; expose final content immediately. Preserve clear state feedback without relying on animationend to complete essential behavior, since reduced motion can remove that event path.

Clean up listeners, observers, timers and animation instances on unmount. Avoid expensive scroll handlers and repeated layout reads/writes. Use profiling for complex effects instead of claiming performance from appearance.

Verify normal and reduced-motion preferences, keyboard input, touch behavior, rapid repeated interactions, interrupted exits and component unmounts where relevant. Report which checks actually ran.
