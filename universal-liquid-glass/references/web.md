# Web Liquid Glass

Use for HTML/CSS/JS, React, Next.js, Vue/Nuxt, Svelte/SvelteKit, Angular, Astro, Solid, Tailwind and browser-based UI.

## Principle

A translucent element with `backdrop-filter: blur(...)` is a **frosted material fallback**, not full refractive Liquid Glass. High-fidelity web glass needs a believable optical edge, crisp foreground content, coherent lighting, restrained depth, and a deliberate compatibility strategy.

## Capability-first decision tree

1. Can the target renderer sample the scene/backdrop through a native or GPU texture? Use Tier B shader refraction.
2. Can the application refract a rendered/captured content layer while keeping semantic DOM on top? Use Tier C content refraction.
3. Does the target browser matrix demonstrably support the exact `backdrop-filter: url(#filter)` path? Tier D may be used.
4. Otherwise use Tier E frosted glass.
5. If reduced transparency/high contrast/performance requires it, use Tier F opaque material.

Do not browser-sniff when feature/probe detection can establish behavior.

## DOM structure

Keep optics and semantics separate:

```html
<div class="glass" data-glass-variant="regular">
  <div class="glass__optics" aria-hidden="true"></div>
  <div class="glass__content">...</div>
</div>
```

Rules:

- `glass__optics` is decorative and `pointer-events: none`.
- `glass__content` contains the real labels, links, buttons and inputs.
- Never duplicate interactive semantic DOM solely to create refraction. If a visual duplicate is unavoidable, hide it from accessibility and hit testing.
- Prefer one reusable primitive/component rather than bespoke filter markup per card.

## Baseline frost fallback

A robust fallback can combine translucency, bounded backdrop blur, saturation/brightness adaptation, a directional rim and soft depth:

```css
.glass {
  position: relative;
  isolation: isolate;
  overflow: clip;
  border-radius: var(--glass-radius, 1.25rem);
  background: color-mix(in srgb, var(--glass-tint, white) 12%, transparent);
  backdrop-filter: blur(var(--glass-blur, 14px)) saturate(1.18);
  -webkit-backdrop-filter: blur(var(--glass-blur, 14px)) saturate(1.18);
  box-shadow:
    inset 0 1px 0 rgb(255 255 255 / .22),
    inset 0 0 0 1px rgb(255 255 255 / .10),
    0 12px 36px rgb(0 0 0 / .12);
}

.glass::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: linear-gradient(160deg, rgb(255 255 255 / .16), transparent 36%);
}
```

Treat values as starting points, not Apple constants. Tune against real backgrounds and device performance.

## Backdrop roots and nesting

CSS backdrop filtering is bounded by the nearest backdrop root. Opacity, masks, filters, `mix-blend-mode`, another backdrop filter, and some `will-change` values can establish a new root. If a nested glass suddenly stops sampling the expected background, inspect ancestor compositing before changing blur values.

Avoid glass-on-glass nesting. It increases compositing cost and often causes confusing sampling boundaries.

## SVG displacement

`feDisplacementMap` displaces one image using channel values from another. A useful glass map has:

- neutral channel values through most of the center;
- a geometry-derived displacement field around the bevel/rim;
- a smooth edge transition;
- stable X/Y channel conventions;
- correct filter color space.

If a displacement map was authored around midpoint byte values in sRGB space, set `color-interpolation-filters="sRGB"`; SVG filter primitives otherwise commonly operate in linearRGB. Validate the result rather than copying channel conventions from another implementation.

### Important distinction

`feDisplacementMap` itself is broadly supported, but applying an SVG URL filter through **backdrop-filter** has different support/behavior than applying an SVG filter to an ordinary rendered element. Do not infer cross-browser backdrop refraction support from generic SVG filter support.

## Portable content-refraction approach

When direct backdrop-SVG behavior is unreliable, render or capture the content to be refracted into an inert visual layer and use the displacement map on that layer while leaving semantic content untouched. The displacement field is portable; the renderer can change between SVG, canvas and WebGL.

This approach is particularly useful when:
- the background is a controlled scene, image, video or canvas;
- the application can cheaply render the scene texture once;
- multiple glass lenses can share the same source texture.

## WebGL/WebGPU shader approach

Use when genuine scene sampling is required and the complexity is justified.

Conceptual pipeline:

```text
scene texture
  -> rounded-shape SDF
  -> edge gradient / normal
  -> UV displacement
  -> 1-3 refracted samples
  -> optional tiny RGB separation at bevel
  -> diffusion/LOD blur
  -> adaptive tint/luminance
  -> specular + edge separation
  -> composite
  -> crisp DOM foreground
```

Performance rules:
- use one shared scene capture for multiple lenses;
- use devicePixelRatio caps for optical buffers;
- resize buffers only on geometry/quality changes;
- do not read pixels back to the CPU every frame;
- pause requestAnimationFrame when no dynamic parameter or source changes;
- prefer lower-resolution optics buffers before removing the effect entirely;
- profile mobile Safari/Chrome and integrated GPUs, not only desktop discrete GPUs.

## React / Next.js

- Keep optical initialization client-side when it requires DOM/WebGL.
- Avoid IDs generated nondeterministically during SSR; stable filter IDs prevent hydration mismatches.
- Use refs and clean up ResizeObserver, pointer listeners, WebGL resources, RAF loops and generated SVG filters on unmount.
- Do not put continuously changing pointer coordinates in React state if they only drive a shader; update refs/uniforms directly.
- Memoize material components and keep content semantics outside the optical renderer.

## Vue / Nuxt

- Initialize browser-only optics in `onMounted`/client-only scope.
- Clean up observers/listeners/resources in `onBeforeUnmount`.
- Keep tuning values in CSS variables or a small typed options object.
- Avoid deep reactive objects for per-frame shader uniforms.

## Svelte / SvelteKit

- Initialize through an action or `onMount` and return cleanup.
- Keep per-frame values outside expensive reactive cascades.
- Use CSS custom properties for semantic variants.

## Angular

- Isolate optics in a component/directive.
- Initialize after the view exists and clean up in destruction hooks.
- Keep animation loops outside unnecessary change detection work.

## Tailwind

Tailwind is suitable for spacing, sizing and semantic surface tokens, but advanced SVG/shader optics should live in a readable component/module rather than an enormous utility string. Prefer semantic classes/tokens for `glass-regular`, `glass-clear`, `glass-prominent`, and quality modes.

## Accessibility CSS

At minimum:

```css
@media (prefers-reduced-motion: reduce) {
  .glass { transition-duration: 0.01ms; }
}

.glass[data-reduce-transparency="true"] {
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
  background: var(--glass-opaque-fallback);
}
```

Browser support for reduced-transparency media queries is not universal. Provide an application-level setting or high-legibility mode when the product requires deterministic support.

## Feature detection

Test each capability you depend on. `CSS.supports('backdrop-filter', 'blur(1px)')` establishes CSS property parsing, not necessarily correct visual behavior of SVG URL backdrop filters. For fragile paths, create a tiny hidden runtime probe or rely on a known renderer path and fall back safely if it fails.

## Anti-patterns

- `backdrop-filter: blur(40px)` on every card.
- giant full-screen glass layer without functional reason.
- refracting/blurring text and icons.
- applying opacity to an entire glass control and accidentally fading foreground contrast.
- `will-change` on every surface.
- a unique SVG filter and RAF loop for every button.
- strong RGB fringe visible before the lensing effect.
- random turbulence used as the primary refraction normal.
- using screenshots as fake live backdrops when content moves.
- claiming Safari/Firefox/Chromium parity without testing the exact implementation.

## Required verification matrix

Test at least:
- Chromium + Safari/WebKit; Firefox when supported by product requirements;
- desktop + mobile;
- light/dark;
- bright, dark, saturated, textured and moving backdrops;
- 1x and high-DPR displays;
- reduced motion and high-legibility mode;
- scrolling while multiple lenses are visible;
- resize/orientation changes;
- keyboard focus and pointer/touch hit testing.
