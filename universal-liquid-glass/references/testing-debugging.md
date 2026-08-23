# Testing and debugging Liquid Glass

Use when an implementation visually fails, behaves differently across browsers/platforms, or performs poorly.

## Debug in layers

Temporarily isolate one material stage at a time:

1. shape/mask only;
2. backdrop/source capture only;
3. displacement/refraction only;
4. diffusion/blur only;
5. tint/luminance adaptation;
6. specular/rim;
7. shadow/depth;
8. interaction animation;
9. foreground semantics.

Do not tune all parameters simultaneously. A broken source texture cannot be repaired by adding more blur.

## Symptom: entire backdrop shifts instead of only the rim

Likely causes:
- displacement-map neutral value does not match the filter's color space;
- X/Y channels are encoded or selected incorrectly;
- map midpoint is not exactly neutral for the chosen renderer;
- filter region/coordinate system differs from map assumptions.

For SVG maps authored around ordinary 8-bit midpoint values, verify `color-interpolation-filters="sRGB"` and channel selectors. Render the map itself onscreen to inspect its center and edges.

## Symptom: glass looks like milk/fog

Likely causes:
- blur/diffusion too strong;
- tint opacity too high;
- no calm/clear center;
- material used over content where standard material would be better;
- multiple nested backdrop filters accumulating.

Fix hierarchy before lowering opacity blindly.

## Symptom: rainbow fringe dominates

Chromatic dispersion is too strong or too wide. Restrict it to a narrow bevel, reduce RGB offset/scale differences, or disable it at balanced quality. Users should perceive a lens before they perceive chromatic aberration.

## Symptom: text/icons look smeared

Foreground content is inside the optical distortion/blur pass. Split the decorative optics layer from the semantic foreground. Refraction belongs to the backdrop/source, not labels.

## Symptom: backdrop filter stops seeing the page background

On web inspect ancestor backdrop roots. Parent opacity, filters, masks, mix-blend-mode, backdrop-filter and some `will-change` values can change the backdrop boundary. Reduce unnecessary compositing and retest.

## Symptom: works in Chromium, fails in Safari/Firefox

Do not assume a generic SVG feature implies SVG URL filters work identically through `backdrop-filter`. Verify the exact path. Use a content-refraction/WebGL renderer or frost fallback instead of browser-specific hacks when broad compatibility is required.

## Symptom: halos/clipped blur at corners

- expand filter/render bounds enough for blur/refraction excursion;
- clip at the intended final material boundary, not too early in the pipeline;
- ensure offscreen buffer padding accounts for maximum displacement + blur radius;
- check premultiplied alpha handling in custom shaders.

## Symptom: geometry changes cause flicker

- keep filter/shader IDs stable;
- resize/reallocate after the new bounds settle;
- avoid destroying and recreating the entire renderer every animation frame;
- use native grouping/morphing APIs on Apple platforms;
- cache maps for recurring sizes if appropriate.

## Symptom: scrolling janks

Inspect:
- total glass pixel area;
- count of independent backdrop filters/offscreen layers;
- buffer DPR/resolution;
- blur radius/sample count;
- per-frame map generation;
- CPU-to-GPU image uploads;
- repeated React/Vue/Svelte state updates from pointer/scroll events;
- shader recompilation;
- live screen capture frame rate.

First reduce repeated surfaces and invalidation. Then reduce optical quality. Do not immediately remove all glass if one architecture mistake causes the cost.

## Symptom: native iOS glass disappears when faded

When using a native wrapper such as current Expo GlassEffect, verify documented opacity behavior. Some native visual-effect implementations do not render when an ancestor is fully transparent. Prefer supported effect-specific animation APIs or transition the surrounding layout without forcing the native glass view to `opacity: 0`.

## Symptom: wrong light/dark appearance during navigation

Synchronize the application's theme provider/window appearance with system appearance before changing material tint. Native glass reacts to environment; an inconsistent theme can appear as flashes/flicker.

## Symptom: desktop glass doesn't show other windows

A webview only knows its own rendered content unless the host provides a real backdrop source. For true desktop refraction, add permissioned wallpaper/screen/window capture plus window-coordinate alignment, or explicitly downgrade to in-app/frosted glass.

## Visual test backgrounds

Maintain a small test scene containing:
- black/white split;
- saturated color blocks;
- fine checker/grid/text pattern;
- large photo;
- animated gradient/video;
- scrolling text/content.

A correct lens should remain defined over all of them without destroying foreground legibility.

## Performance test scene

Test one, four and the maximum expected number of simultaneous lenses; static and scrolling backdrop; full and balanced quality; minimum target device; resize/orientation; idle state. Confirm the render loop/capture pipeline parks when nothing changes.

## Final debugging rule

If the exact renderer limitation cannot be overcome without fragile/private behavior, document it and use the next fidelity tier. A stable intentional fallback is better than a demo-only effect that breaks semantics or compatibility.
