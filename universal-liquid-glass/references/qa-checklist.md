# Required QA checklist

Use before declaring work complete.

## Hierarchy
- [ ] Glass is concentrated on functional controls/navigation.
- [ ] Content remains the visual focus.
- [ ] Primary action is clear without tinting everything.
- [ ] Content-layer cards/panels are not glass by default.
- [ ] Edge-to-edge/scroll-under behavior is intentional.

## Optics
- [ ] Foreground labels/icons are crisp.
- [ ] Refraction is shape-aware and strongest near the rim.
- [ ] Center is calmer than bevel.
- [ ] Blur supports diffusion rather than being the only glass cue.
- [ ] Specular lighting has coherent direction.
- [ ] Chromatic dispersion is subtle.
- [ ] No random neon/rainbow outline masquerades as glass.
- [ ] Result is correctly labeled native vs emulated.

## Geometry
- [ ] Radii/inner geometry are visually concentric.
- [ ] Compact controls use appropriate continuous/capsule/circle shapes.
- [ ] No accidental glass-on-glass nesting.
- [ ] Morphing groups use platform grouping/container primitives when available.

## Color and themes
- [ ] Neutral glass avoids unnecessary fixed color.
- [ ] Tint is semantic/sparing.
- [ ] Tested over bright/dark/saturated/textured backdrops.
- [ ] Light/dark/increased-contrast themes are handled.
- [ ] Larger surfaces have enough diffusion/separation.

## Interaction
- [ ] Touch response is tactile but restrained.
- [ ] Pointer response is less exaggerated.
- [ ] Animations are brief and interruptible.
- [ ] No idle wobble/continuous jello.
- [ ] Optical layers do not intercept events.

## Accessibility
- [ ] Roles/labels/reading order are intact.
- [ ] Keyboard/focus navigation remains visible.
- [ ] Contrast is safe across realistic backgrounds.
- [ ] Reduced motion is honored.
- [ ] Reduced transparency/high contrast has deliberate fallback.
- [ ] State is not communicated by transparency/color alone.
- [ ] Duplicated visual content is hidden from accessibility/focus.

## Performance
- [ ] Expensive effects are bounded.
- [ ] Maps/shaders are reused/cached.
- [ ] Translation does not regenerate shape maps.
- [ ] Multiple lenses share backdrop/scene work where possible.
- [ ] Render loops park/reduce when static.
- [ ] Minimum target hardware is profiled or conservative fallback provided.
- [ ] Quality degradation preserves function/hierarchy.

## Compatibility and delivery
- [ ] Native Apple APIs preferred where appropriate.
- [ ] Browser/API support feature-detected.
- [ ] SVG-backdrop refraction not claimed cross-browser without proof.
- [ ] Unsupported platforms get frost/opaque fallback.
- [ ] Current package versions verified before dependencies.
- [ ] Fidelity tiers, limitations, fallbacks and verification matrix documented.
