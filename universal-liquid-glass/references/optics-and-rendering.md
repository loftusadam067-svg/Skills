# Optics and rendering

Portable conceptual pipeline:

```text
scene/backdrop source
  -> shape mask / signed distance
  -> bevel + edge normal/displacement field
  -> refracted source samples
  -> optional tiny spectral/RGB separation
  -> controlled diffusion/scattering
  -> adaptive tint/luminosity
  -> specular + darker edge separation
  -> ambient depth/shadow
  -> crisp semantic foreground UI
```

The exact renderer changes by platform; the hierarchy of effects should remain intelligible.

## Source ownership

Before implementing refraction, identify what pixels can actually be sampled.

- Native Apple system material: let the OS own source sampling.
- Web backdrop filter: browser owns the backdrop within backdrop-root rules.
- GPU scene: application owns a texture/framebuffer and can sample displaced UVs.
- Controlled DOM/content-refraction: app creates an inert rendered copy/source while semantic DOM remains above it.
- Desktop “real world” backdrop: host must provide wallpaper/screen/window capture and coordinate alignment.

A shader cannot refract pixels it never receives.

## Signed distance / geometry field

For a rounded rectangle or capsule, derive a signed-distance function (SDF) or equivalent shape distance. Use the spatial gradient of distance as an approximate 2D surface normal.

Desired profile:
- broad neutral/low-displacement center;
- smooth rise through a bevel band;
- strongest apparent lensing near the visually thick edge;
- clean decay/clamp outside the shape;
- corner behavior follows the same geometry rather than switching to arbitrary turbulence.

The normal/displacement field should come from shape geometry. Noise can add subtle imperfection but must not define the lens.

## Refraction model

For a 2D emulation, displacement can be conceptualized as:

```text
uv_refracted = uv + normal.xy * edgeStrength * refractionScale
```

where `edgeStrength` is near zero in the central plateau and increases through the bevel. More physically inspired renderers can model thickness/index-of-refraction, but UI fidelity usually benefits more from stable shape-aware lensing than from an expensive literal simulation.

Avoid large displacement that makes content appear detached from its source or causes severe edge clipping.

## Displacement maps

A portable map can encode X/Y displacement in two color channels.

Rules:
- define the neutral channel value explicitly;
- keep most of the interior near neutral;
- reserve strong deviation for the bevel;
- document X/Y channel selectors;
- account for filter color space;
- include sufficient padding/filter bounds for maximum displacement and blur;
- regenerate only when geometry/quality changes.

For SVG `feDisplacementMap`, channel values are interpreted through the filter's color space. SVG filter primitives commonly default to linearRGB. If the map was authored around ordinary sRGB byte midpoint values, use `color-interpolation-filters="sRGB"` and verify visually.

## Chromatic dispersion

Liquid Glass can show subtle spectral separation around high-gradient edges. Emulate it sparingly:

- sample R/G/B with tiny differences in refraction strength or UV offset;
- mask it tightly to the bevel/rim;
- converge channels through the center;
- remove it entirely at balanced/fallback quality;
- avoid visible rainbow outlines on low-contrast backgrounds.

If users perceive RGB fringe before lensing, reduce it.

## Diffusion / scattering

Blur is a legibility/scattering term, not refraction.

- Use bounded/clipped diffusion.
- Compact clear/media controls can be less diffuse.
- Larger/thicker surfaces need more diffusion and edge/depth separation.
- Prefer lower-resolution or mip/LOD sampling in GPU renderers over huge multi-pass Gaussian kernels when possible.
- Do not compensate for a broken lens by making the glass opaque and blurry.

## Adaptive tint and luminance

The material should respond to its environment while preserving semantic intent.

Possible inputs:
- local sampled luminance/chroma;
- system light/dark mode;
- semantic tint/prominence;
- accessibility high-legibility mode.

Keep adaptation temporally stable. Avoid per-frame foreground color flicker as a moving high-frequency backdrop crosses the lens; use smoothing/hysteresis or stronger diffusion if necessary.

## Specular response

Where geometry is available, derive highlight intensity from normal and a coherent light direction, then shape it nonlinearly and mask to the bevel. A restrained gradient sheen is acceptable in simpler renderers.

Pair a brighter specular response with a subtle darker separation edge or soft shadow. Larger surfaces can use stronger/deeper cues than tiny buttons.

## Premultiplied alpha

Custom GPU pipelines often operate with premultiplied alpha. Halos can appear when blur/refraction mixes transparent pixels incorrectly. Verify:
- texture alpha convention;
- blending mode;
- whether color channels are un/premultiplied before math;
- render-target clear color;
- padding outside the shape.

## Scene texture strategy

For multiple lenses, render/capture the scene **once** where possible and sample it from several lenses. Independent screen/DOM captures per lens are usually wasteful and can desynchronize.

For dynamic scenes:
- update the source only as often as it visibly changes;
- avoid CPU readback;
- reuse texture allocations;
- cap optical resolution independently from UI text resolution.

## Interaction

Interaction should modulate material parameters rather than recreate the entire renderer.

Examples:
- slight edge refraction increase on press;
- specular highlight movement/intensity change;
- small shape/thickness response;
- related glass shape morphing.

Keep hit target geometry stable. Update uniforms/parameters, not map pixels, unless geometry actually changed.

## Quality tiers

### Full
- source refraction;
- shape-aware normals/SDF;
- subtle dispersion;
- controlled diffusion;
- adaptive tint/luminance;
- dynamic specular/depth;
- interactive response.

### Balanced
- lower optical buffer resolution;
- one primary refracted sample;
- no/minimal dispersion;
- simpler specular;
- same semantic hierarchy.

### Frost
- no refraction;
- bounded backdrop blur/diffusion;
- adaptive tint;
- coherent rim and shadow;
- crisp foreground.

### Opaque
- no scene sampling;
- semantic high-contrast fill;
- same geometry, grouping and interaction.

## Numerical tuning rule

Do not expose arbitrary optical numbers as product-level API. Build semantic variants and tune renderer internals against a test scene. Numeric values in community demos are implementation-specific and should never be labeled official Apple constants.

## Optical acceptance tests

A good material should:
- remain visible over both light and dark backgrounds;
- reveal edge lensing without making the center unreadable;
- keep labels/icons perfectly crisp;
- avoid color fringing on flat backgrounds;
- preserve a coherent light direction across related surfaces;
- show stronger depth cues as a surface becomes larger/thicker;
- degrade gracefully when refraction/blur is disabled.
