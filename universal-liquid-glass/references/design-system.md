# Liquid Glass design system

Treat Liquid Glass as a **functional layer** floating above a **content layer**. Good candidates: navigation/tab bars, toolbars, search, floating primary actions, popovers/menus/contextual controls, media controls, transient sliders/toggles/selection lenses. Usually not glass: article/body backgrounds, every content card, dense data tables, large static sections, decorative noninteractive panels.

## Variants

**Regular:** default for complex backgrounds, meaningful text, larger functional surfaces and maximum readability.

**Clear/media:** only over visually rich media when revealing media matters, controls are compact, contrast is safe, and adaptive dimming can be added.

**Prominent/tinted:** reserve for primary action, selected/active state, or meaningful semantic emphasis. Do not tint entire toolbars.

## Geometry

Use capsule/circle/continuous rounded geometry for compact controls and continuous rounded rectangles for panels. Preserve concentricity. Avoid unrelated stacked rounded rectangles and accidental glass-on-glass nesting. Use native grouping/container effects where possible.

## Edge-to-edge

Glass reads best when meaningful content can move beneath it. Prefer edge-to-edge scrolling content, floating controls rather than opaque bars, and platform scroll-edge legibility treatments. Avoid decorative glass strips over empty backgrounds.

## Color and adaptation

Native Liquid Glass has no fixed inherent color; it responds to backdrop/system settings. Emulations should adapt to backdrop luminance where practical, keep neutral glass neutral, use semantic color sparingly, test bright/dark/saturated/patterned/moving backdrops, and give larger surfaces more diffusion/opacity than compact controls. Avoid rainbow outlines, default neon glow, ubiquitous saturated gradients, and fixed white tint.

## Specular and depth

Use coherent directional specular rim/sheen, subtle darker edge/depth separation, restrained ambient shadow, and stronger separation for larger/thicker surfaces. A uniform bright border alone is not an optical model.

## Motion

Use motion to reinforce direct manipulation: tactile touch response, restrained pointer response, brief precise transitions, related-control morphing, interruptibility. Avoid permanent wobble, universal jelly physics, long bounce chains, giant parallax, and motion required to understand state.

## Responsive design

Adapt across phone portrait/landscape, tablet split/resizable windows, desktop, pointer/touch and size classes/breakpoints. Prefer semantic layout decisions over device-model checks.

## Anti-slop

Reject default hero + glass-card grids + giant glass CTA patterns; universal translucency; arbitrary blur without backdrop testing; oversized radii everywhere; thin illegible text over imagery; glowing edges pretending to be refraction; random RGB fringing; decorative glass with no hierarchy/function; and huge static glass regions that reduce readability.
