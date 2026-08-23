# Required QA checklist

Run this before declaring Liquid Glass work complete. For complex implementations also score `../evals/evaluation-rubric.md`.

## 1. Classification and fidelity
- [ ] Target framework/renderer and minimum OS/browser versions are known.
- [ ] Native vs emulated material is labeled accurately.
- [ ] Selected fidelity tier A-F is stated for each target.
- [ ] The selected renderer can actually access the backdrop/source pixels it intends to refract.
- [ ] Current dependency/API requirements were verified when version-specific guidance matters.

## 2. Hierarchy
- [ ] Glass is concentrated on functional controls/navigation.
- [ ] Content remains the visual focus.
- [ ] Content-layer cards/panels are not glass by default.
- [ ] Primary action is clear without tinting everything.
- [ ] Regular/clear/prominent variants have semantic reasons.
- [ ] Edge-to-edge/scroll-under behavior is intentional where used.
- [ ] No decorative glass region exists solely because “Liquid Glass” was requested.

## 3. Native platform use
- [ ] Apple-native implementation prefers current system components before custom effects.
- [ ] No duplicate custom glass is layered behind system controls that already receive system glass.
- [ ] Custom Apple glass uses public APIs only.
- [ ] Nearby related native glass elements use grouping/container APIs when appropriate.
- [ ] No reverse-engineered numeric values are described as official Apple constants.
- [ ] Non-Apple material is described as an emulation/fallback, not native Apple Liquid Glass.

## 4. Optics
- [ ] Foreground labels/icons are crisp and outside destructive optical passes.
- [ ] Refraction is shape-aware and strongest around the bevel/rim.
- [ ] Center is calmer than the edge.
- [ ] Displacement map/channel conventions are documented and correct.
- [ ] SVG filter color-space behavior is correct for the map encoding.
- [ ] Blur supports diffusion/legibility rather than being the only glass cue.
- [ ] Specular lighting has a coherent direction.
- [ ] Darker edge/depth separation or shadow is restrained and coherent.
- [ ] Chromatic dispersion is subtle and localized.
- [ ] No random turbulence/neon/rainbow outline masquerades as glass.
- [ ] Filter/render bounds account for displacement + blur and do not clip halos.
- [ ] Premultiplied-alpha/compositing behavior does not create edge artifacts.

## 5. Geometry and grouping
- [ ] Radii/inner geometry are visually concentric.
- [ ] Compact controls use appropriate continuous/capsule/circle shapes.
- [ ] Larger surfaces use geometry appropriate to their size/context.
- [ ] No accidental glass-on-glass nesting.
- [ ] Morphing only connects related states/elements.
- [ ] Group boundaries correspond to functional grouping rather than arbitrary proximity.
- [ ] Hit target geometry remains stable while the material animates.

## 6. Color, themes and dynamic backdrops
- [ ] Neutral glass avoids unnecessary fixed color.
- [ ] Tint is semantic and sparing.
- [ ] Tested over bright, dark, saturated, textured and moving backdrops.
- [ ] Light/dark appearance is handled.
- [ ] Increased-contrast/high-legibility mode is handled.
- [ ] Larger surfaces receive enough diffusion/depth separation.
- [ ] Foreground color does not flicker as background content moves.
- [ ] Theme transitions do not flash a mismatched native material appearance.

## 7. Interaction and motion
- [ ] Touch response is tactile but restrained.
- [ ] Pointer response is less exaggerated than direct touch where appropriate.
- [ ] Animations are brief and interruptible.
- [ ] No idle wobble/continuous jello/noise animation by default.
- [ ] No cursor-following distortion across the whole page/app.
- [ ] Optical layers do not intercept pointer/touch events.
- [ ] Reduced-motion mode removes nonessential morphing/continuous effects.

## 8. Accessibility
- [ ] Roles, labels and reading order are intact.
- [ ] Keyboard/focus navigation remains visible and functional.
- [ ] Screen reader/TalkBack/VoiceOver semantics are not duplicated by decorative layers.
- [ ] Contrast is safe across realistic dynamic backgrounds.
- [ ] Reduced transparency/high contrast has a deliberate fallback.
- [ ] State is not communicated by transparency/color/refraction alone.
- [ ] Duplicated visual content is hidden from accessibility/focus.
- [ ] Text scaling/Dynamic Type does not clip controls.
- [ ] Long/localized/RTL content is considered where relevant.
- [ ] Touch targets remain platform-appropriate after visual styling.

## 9. Performance and lifecycle
- [ ] Expensive effects are tightly bounded.
- [ ] Maps, masks, buffers and shader programs are reused/cached.
- [ ] Translation-only movement does not regenerate geometry-dependent maps.
- [ ] Multiple lenses share backdrop/scene work where possible.
- [ ] Optical buffer DPR/resolution is capped/adaptive where needed.
- [ ] No per-frame CPU pixel readback unless explicitly justified.
- [ ] No per-frame shader recompilation.
- [ ] Render loops/tickers/capture pipelines park or reduce when static/hidden.
- [ ] ResizeObserver/listeners/RAF/GPU/native resources are cleaned up on disposal.
- [ ] Repeated scrolling rows do not each run expensive full-quality glass without profiling.
- [ ] Minimum target hardware is profiled or conservative fallback is provided.
- [ ] Quality degradation preserves function/hierarchy/layout.
- [ ] Sustained scrolling/thermal behavior is acceptable for persistent effects.

## 10. Web compatibility
- [ ] `backdrop-filter`/SVG paths are feature- or behavior-detected as needed.
- [ ] Generic SVG filter support is not treated as proof of SVG-backdrop support.
- [ ] Backdrop-root/compositor ancestors were checked if sampling is wrong.
- [ ] Chromium/WebKit/Firefox requirements are tested according to product matrix.
- [ ] SSR/hydration uses stable IDs/resources in frameworks that render on the server.
- [ ] Web optical layers preserve selection, links, inputs and hit testing.

## 11. Mobile/cross-platform compatibility
- [ ] Expo/RN native glass requirements are checked against the installed SDK/build type.
- [ ] Native iOS material is not duplicated by custom BlurView/GlassView under native tabs/headers.
- [ ] Flutter renderer/native bridge choice is explicit.
- [ ] Android API level and AGSL/RuntimeShader availability are respected.
- [ ] Unsupported platforms receive frost/opaque fallback without layout breakage.
- [ ] Orientation, safe areas and keyboard changes are handled.

## 12. Desktop/hybrid compatibility
- [ ] In-app backdrop vs real desktop backdrop is explicitly distinguished.
- [ ] Real desktop refraction has a host-provided source rather than impossible CSS assumptions.
- [ ] Screen-capture permission denial has a safe fallback.
- [ ] Multi-monitor DPI/window-position changes remain aligned.
- [ ] Capture/rendering pauses when minimized/hidden where possible.

## 13. Code and maintainability
- [ ] One reusable semantic material primitive/modifier/component exists.
- [ ] Low-level optical magic numbers are not scattered across app code.
- [ ] Existing state/routing/component conventions are preserved.
- [ ] Added dependencies are justified, current and appropriately licensed.
- [ ] No opaque/minified/private implementation is copied without understanding it.
- [ ] Renderer-specific complexity is isolated behind the semantic API.

## 14. Delivery and reporting
- [ ] Fidelity tiers, APIs/renderers and fallbacks are documented.
- [ ] Accessibility behavior is documented.
- [ ] Performance/quality strategy is documented.
- [ ] Tested vs untested targets are explicit.
- [ ] Known renderer limitations are stated rather than hidden.
- [ ] No file path referenced by the delivered skill/package is missing.

## Hard-fail conditions

Do not declare completion if any are true:
- blur-only frost is presented as true/native Liquid Glass;
- foreground text/icons are refracted or blurred destructively;
- a required target has no functioning fallback;
- accessibility semantics/focus are broken;
- private Apple APIs are used for production guidance;
- an expensive unbounded effect is knowingly shipped without justification/fallback;
- an installable skill/package contains dangling references or unresolved placeholders.
