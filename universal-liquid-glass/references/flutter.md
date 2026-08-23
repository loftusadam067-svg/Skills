# Flutter Liquid Glass

Use for Flutter mobile, desktop and web. Distinguish native Apple material from Flutter-rendered emulation.

## Strategy

Choose in this order:

1. **Native Apple bridge/platform view** when exact system Liquid Glass behavior is a hard requirement on supported Apple OS versions.
2. **Flutter shader/backdrop emulation** when a consistent cross-platform appearance is more important than native identity.
3. **Bounded BackdropFilter/frost** for broad compatibility and lower cost.
4. **Opaque semantic fallback** for accessibility or weak rendering paths.

Do not assume a Cupertino-styled Flutter widget automatically matches the current Apple Liquid Glass implementation. Verify the current Flutter SDK and package behavior.

## Architecture

Create one semantic widget, for example `LiquidGlass`, with variants such as regular/clear/prominent and a quality policy. Internally select the platform renderer. Keep child content outside destructive shader/filter passes.

```dart
LiquidGlass(
  variant: GlassVariant.regular,
  quality: GlassQuality.auto,
  child: const Icon(Icons.search),
)
```

## BackdropFilter path

Use `BackdropFilter` only for bounded regions and clip it to the intended shape. A backdrop blur is a frost fallback, not true refraction.

Rules:
- clip before/around the backdrop filter so sampling is bounded;
- avoid a full-screen high-sigma blur for a small control;
- group/shared-backdrop mechanisms where the current Flutter version provides them;
- keep foreground text/icons in an unblurred layer;
- test scrolling because repeated backdrop filters can be expensive.

## FragmentShader / custom shader path

For high-fidelity emulation:

1. obtain a scene texture or render the controlled background to an image/texture;
2. derive a rounded-shape SDF and edge normal;
3. displace UVs near the rim;
4. optionally use tiny RGB sample separation near the bevel;
5. add controlled diffusion, tint and specular response;
6. composite semantic child content afterward.

Prefer a single shared shader program/runtime effect and update uniforms instead of recompiling per frame. Reuse textures and render targets. Cap internal render resolution on high-DPR devices when quality/performance warrants it.

## CustomPainter / ImageFiltered

`ImageFiltered` affects its child rather than the content behind it; use it for controlled visual layers, not as a direct substitute for backdrop sampling. `CustomPainter` is appropriate for rim/specular/decorative layers but does not provide true live backdrop refraction by itself.

## Native Apple bridge

When exact Apple material is required:
- use public UIKit/AppKit APIs through a maintained plugin or a small platform implementation;
- expose semantic variant/tint/interactive options only;
- preserve Flutter semantics on the foreground or ensure native accessibility is correctly integrated;
- avoid large numbers of platform views in scrolling lists;
- verify compositing with transforms, clips and animations;
- provide a Flutter fallback for older Apple OS versions and non-Apple platforms.

Verify community packages before use. Check maintenance, license, minimum Flutter/Xcode/iOS versions, Impeller compatibility, platform-view behavior, and whether public native APIs are used.

## Impeller and renderer behavior

Profile using the renderer actually shipped by the target Flutter release. Shader compilation, texture sampling and blur behavior can differ across backends. Warm/prepare shaders if the current toolchain supports it and startup jank is observed.

## Web

Flutter web follows the browser's actual rendering capabilities. CanvasKit/WebGL/WebGPU paths do not make CSS backdrop behavior available automatically. If the scene is already renderer-owned, shader-based refraction may be more reliable than trying to mix DOM backdrop filters with canvas content.

## Accessibility

- Keep semantics attached to the real child controls.
- Respect platform text scaling.
- For reduced motion, disable decorative morphing/continuous shader animation.
- Provide an opaque/high-legibility mode.
- Do not use refraction, tint or transparency alone to communicate selected/disabled/error state.

## Performance checklist

- No expensive glass per scrolling list row by default.
- Blur/filter bounds clipped tightly.
- Shader programs reused.
- Texture captures shared.
- DevicePixelRatio/internal render scale capped adaptively.
- No CPU pixel readback in the animation loop.
- Render loop stops when static/offscreen.
- Release/profile mode tested on minimum hardware.

## Verification

Test iOS native/fallback, Android, desktop targets if supported, web renderer if shipped, resize/orientation, scrolling, light/dark, accessibility settings, high-DPR devices and memory/resource cleanup.
