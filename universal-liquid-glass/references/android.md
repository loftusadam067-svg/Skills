# Android and Jetpack Compose Liquid Glass emulation

Use for Android Views, Jetpack Compose and Compose Multiplatform. Android does not provide Apple's native Liquid Glass material; describe the result as an emulation.

## Renderer selection

Preferred order:

1. Android/Compose shader path using public graphics APIs when the minimum API and performance budget support it.
2. Bounded blur/backdrop capture plus custom rim/specular rendering.
3. Translucent/opaque Material surface preserving hierarchy.

Keep the component API semantic so the app can use the same `regular`, `clear/media`, `prominent`, and quality variants across platforms.

## AGSL / RuntimeShader

Android 13 / API 33 introduced `RuntimeShader` using Android Graphics Shading Language (AGSL). AGSL resembles GLSL but participates in Android's Canvas/RenderNode pipeline. It can drive custom per-pixel effects and be used with rendering APIs such as `RenderEffect`.

Use it for:
- geometry-aware edge deformation;
- tint/specular calculations;
- controlled diffusion when the source texture/render node is available;
- interactive parameters updated through uniforms.

Do not assume AGSL can sample arbitrary pixels behind an unrelated view. Define exactly which source/render node is being sampled.

## Compose

Current Compose graphics APIs can use shaders/brushes and draw-cache patterns. For an emulated glass component:

- use `drawWithCache` or equivalent to avoid recreating brushes/shaders every frame;
- update small uniforms for pointer/press animation rather than rebuilding the whole shader;
- clip to a continuous rounded shape;
- render the optical/decorative layer behind semantic content;
- preserve `Modifier.semantics`, focus, click and touch target behavior;
- use `graphicsLayer` only when it solves a real compositing need.

## RenderEffect considerations

Applying a `RuntimeShader` through `RenderEffect` to a parent and all children can be more expensive than drawing a dedicated custom layer. Prefer the smallest affected render subtree. Never put a heavy effect on the entire activity merely to render a small search pill.

## Pre-API-33 fallback

Do not attempt to force AGSL onto unsupported devices. Options include:
- platform blur capabilities where available;
- controlled screenshot/scene texture approaches if the app already owns the scene;
- simpler translucent Material surfaces;
- opaque high-contrast fallback.

Avoid adding a large graphics dependency solely for a decorative effect unless product requirements justify it.

## Material integration

The UI should still feel native to Android:
- preserve Android navigation conventions, ripple/indication semantics where appropriate, typography and accessibility;
- do not force iOS control geometry onto every Android component;
- use Liquid Glass optics as a visual treatment while retaining platform-appropriate interaction patterns.

## Backdrop capture

If high-fidelity refraction needs live content behind the lens, prefer sharing a renderer-owned source rather than repeatedly capturing the whole window. Repeated bitmap screenshots are memory-bandwidth heavy and can lag one or more frames behind motion.

When using an offscreen layer/texture:
- keep capture region bounded;
- reuse allocations;
- avoid CPU readback;
- synchronize transforms precisely;
- update only when the source changes.

## Accessibility

- Preserve TalkBack semantics and focus order.
- Keep foreground text/icons out of shader distortion.
- Respect animator duration scale/reduced-motion equivalents.
- Maintain contrast over dynamic backgrounds and expose a high-legibility/opaque mode.
- Ensure selected/disabled/error states remain understandable without transparency or tint.

## Performance

- Cache shader objects and geometry.
- Limit simultaneous refractive surfaces.
- Prefer a shared source texture for several lenses.
- Reduce internal optical render scale before removing semantics/interaction.
- Stop continuous animation when offscreen or static.
- Test thermal behavior and sustained scrolling, not only a static preview.

## Compose Multiplatform

Treat each target renderer separately. Android may use AGSL; desktop may use Skia/shader paths; Apple targets should use a verified native bridge if exact native Liquid Glass is required. Share semantic design tokens and component behavior, not one forced renderer.

## Verification

Test minimum API, API 33+, representative low/mid/high GPUs, 60/90/120 Hz devices where relevant, scrolling, configuration changes, font scaling, TalkBack, dark/light themes, battery/thermal behavior and fallback selection.
