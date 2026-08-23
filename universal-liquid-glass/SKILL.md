---
name: universal-liquid-glass
description: Design, implement, debug, audit, or refactor high-fidelity Apple-style Liquid Glass interfaces across SwiftUI/UIKit/AppKit, HTML/CSS/JS and web frameworks, React Native/Expo, Flutter, Android/Compose, Electron/Tauri, Qt/QML, .NET and other frontend stacks. Use for Liquid Glass, iOS 26+ / current Apple glass, refractive or frosted glass, glass navigation/toolbars/tab bars/controls, shader or SVG displacement/refraction, glass performance/compatibility bugs, or converting an existing UI to Liquid Glass while preserving accessibility, semantics and performance.
license: MIT
compatibility: Kimi Agent, Kimi Code, and Agent Skills-compatible coding agents. Implementations may require current platform/browser feature detection, GPU APIs, native build tooling, or deliberate fallbacks.
metadata:
  version: "3.0.0"
  research-date: "2026-08-23"
---

# Universal Liquid Glass

Build Liquid Glass as a **functional, adaptive material system**, not generic glassmorphism. Match Apple's current design intent on Apple platforms and reproduce the same hierarchy/optical principles elsewhere only as far as the target renderer can support them. Never claim an emulation is Apple's native material.

## 1. Classify before designing or coding

Determine:

- task: design, implementation, debugging, audit/refactor, or explanation;
- frontend/framework and renderer;
- target OS/browser versions and minimum deployment target;
- Apple-native vs cross-platform requirements;
- existing architecture, component system, tokens, state, routing and animation library;
- dependency restrictions and whether current docs/packages can be checked;
- minimum device/GPU/performance budget;
- touch/pointer/keyboard and responsive/window-size requirements;
- light/dark/high-contrast/reduced-motion/reduced-transparency behavior;
- whether the UI is primarily content, media, or controls.

Do not select a rendering technique before identifying the target matrix. Preserve existing architecture and semantics unless changing them is necessary.

## 2. Use the content-layer / functional-layer model

**Content layer:** reading surfaces, data, media, lists, tables, article/app backgrounds, ordinary content cards.

**Functional layer:** navigation, tab bars, toolbars, search, floating actions, menus/popovers, segmented controls, transient media/editing controls and important controls over content.

Liquid Glass belongs primarily to the **functional layer**. Do not make every card, panel or section glass. A request to “make all the cards Liquid Glass” should be evaluated, not obeyed mechanically.

Read `references/design-system.md` for hierarchy, variants, geometry, color, motion and anti-slop rules.

## 3. Choose the highest viable fidelity tier

State the selected tier when implementing.

### Tier A — Native system Liquid Glass

Use current public Apple system components/APIs or a verified native bridge. This is the only tier that should be called native Apple Liquid Glass.

### Tier B — True refractive renderer

Use a scene/backdrop texture with Metal, AGSL, SkSL/Flutter shaders, GLSL/WebGL, WebGPU, canvas/GPU or equivalent. Sample displaced source pixels using geometry-aware edge normals.

### Tier C — Portable content refraction

Refract a controlled rendered/captured content layer with a portable displacement field while leaving semantic foreground content crisp. Useful when direct backdrop filtering is not portable.

### Tier D — Direct backdrop SVG refraction

Use `backdrop-filter: url(#...)`/SVG displacement only after verifying the **exact target browser behavior**, not merely generic SVG-filter support.

### Tier E — High-quality frost

Use bounded backdrop blur, adaptive tint/luminance, restrained saturation, coherent rim/specular cues and depth. This is a fallback material, **not true refraction**.

### Tier F — Opaque/high-legibility fallback

Use when transparency is reduced/disabled, rendering support is absent, performance is insufficient, or dynamic contrast cannot be made reliable.

Never distort foreground text/icons to fake refraction.

## 4. Material anatomy

A high-fidelity non-native material should conceptually separate:

1. backdrop/scene source;
2. shape mask / signed-distance geometry;
3. edge normal or displacement field;
4. refraction strongest near the rim with a calmer center;
5. optional tiny chromatic dispersion near the bevel;
6. controlled diffusion/frost for legibility;
7. adaptive tint/luminosity;
8. coherent specular highlight and darker edge/depth separation;
9. restrained shadow/elevation;
10. crisp semantic foreground content;
11. subtle interaction response;
12. accessibility/performance adaptation.

Read `references/optics-and-rendering.md` for implementation details.

## 5. Platform routing

Load only the references needed for the target.

| Target/problem | Required reference |
|---|---|
| SwiftUI, UIKit, AppKit, iOS/iPadOS/macOS | `references/apple-native.md` |
| HTML/CSS/JS, React, Next, Vue, Svelte, Angular, Astro, Tailwind | `references/web.md` |
| React Native, Expo, Expo Router, Capacitor | `references/react-native.md` |
| Flutter | `references/flutter.md` |
| Android Views, Jetpack Compose, Compose Multiplatform | `references/android.md` |
| Electron, Tauri, pywebview, Qt/QML, .NET desktop/hybrid | `references/desktop-hybrid.md` |
| Any accessibility/performance-sensitive task | `references/accessibility-performance.md` |
| Visual/rendering bugs or jank | `references/testing-debugging.md` |
| Current API/dependency claims or research provenance | `references/sources.md` |
| Final completion audit | `references/qa-checklist.md` |
| Complex/high-stakes implementation evaluation | `evals/evaluation-rubric.md` |

## 6. Apple-native rule

On supported Apple platforms, use system components before custom effects. Current SwiftUI/UIKit/AppKit components can adopt Liquid Glass automatically.

For custom SwiftUI glass, prefer public APIs such as `glassEffect(_:in:)`, `.regular` by default, `.clear` only in appropriate media-rich contexts, semantic tinting, `.interactive()` on real interactive custom controls, and `GlassEffectContainer` for related nearby shapes. Prefer native glass button styles for buttons rather than putting a button on an arbitrary glass plate.

For UIKit/AppKit use current public glass effect/container APIs where the deployment target supports them. Do not use private APIs or freeze reverse-engineered Apple constants. Apple's material evolves across OS releases; let system rendering own that evolution.

Read `references/apple-native.md` before Apple-native implementation.

## 7. Web rule

Do not equate `backdrop-filter: blur(...)` with true Liquid Glass.

For real optical refraction, use geometry-aware displacement/shader/content sampling, keep the central plateau calm, keep semantics above the optics, feature/probe-detect fragile paths and provide frost/opaque fallbacks.

With SVG `feDisplacementMap`, understand channel encoding and filter color space. Generic `feDisplacementMap` support does **not** prove that SVG URL filters behave identically through `backdrop-filter` across browsers.

Read `references/web.md` before high-fidelity web implementation.

## 8. Cross-platform rule

Share **semantic design tokens and component behavior**, not one forced renderer.

- React Native/Expo: prefer verified native iOS glass when supported; use Android/web fallbacks per platform.
- Flutter: choose native Apple bridge for exact native fidelity or a renderer-owned shader for cross-platform consistency.
- Android/Compose: use public Android shader/graphics capabilities where viable; describe the result as an emulation.
- Desktop/hybrid: distinguish refracting in-app content from refracting the actual desktop. A webview cannot see arbitrary pixels behind its window without a host-provided backdrop source.

## 9. Accessibility invariants

Preserve roles, names, reading order, focus, keyboard/touch behavior, text selection, font scaling and localization. Optical layers must be decorative/noninteractive.

Never encode meaning only through tint, color, transparency or refraction. Test legibility over bright, dark, saturated, textured and moving backdrops. Respect reduced motion. Use native reduced-transparency/high-contrast adaptation where available and provide an explicit high-legibility/opaque path where signals are not reliably exposed.

Read `references/accessibility-performance.md` for every production implementation.

## 10. Performance invariants

Prefer native compositor paths. Bound sampled area. Share backdrop/scene captures across lenses. Cache geometry-dependent maps, masks, shader programs and buffers. Do not regenerate displacement maps for translation-only motion. Avoid high-cost glass in repeated list rows. Cap optical buffer resolution when needed. Pause RAF/display-link/ticker/capture loops when static or hidden.

Degrade predictably:

1. remove decorative continuous animation;
2. lower optical render resolution;
3. remove/reduce dispersion and secondary samples;
4. simplify specular/diffusion;
5. turn secondary surfaces into frost;
6. switch to opaque fallback.

Preserve function, geometry and hierarchy at every tier.

## 11. Motion and interaction

Use short direct press responses, restrained pointer effects, related-shape morphs and interruptible transitions. Avoid idle wobble, universal jelly physics, exaggerated cursor magnetism, constant animated noise and movement that destabilizes hit targets.

## 12. Freshness and dependency policy

When web/current documentation access exists and the answer depends on a package/API version, verify it. Inspect the project's actual versions first.

Do not:
- recommend a community package solely because it appears in this skill's research sources;
- copy private/minified/opaque shaders without understanding license and behavior;
- treat beta/preview APIs as stable without saying so;
- infer platform support from a similar API on another renderer.

Prefer first-party docs, current standards and maintained public APIs. See `references/sources.md`.

## 13. Implementation procedure

1. Inspect project and target matrix.
2. Classify candidate surfaces as content vs functional.
3. Load the relevant platform reference(s).
4. Choose and state fidelity tier per target.
5. Define semantic variants/tokens and fallback mapping.
6. Implement one reusable material primitive/modifier/component.
7. Keep optics separate from semantic foreground.
8. Add responsive, theme, accessibility and compatibility behavior.
9. Integrate existing state/component/animation systems.
10. Clean up renderer resources/listeners/observers on disposal.
11. Profile the expensive path on minimum hardware or use conservative fallback.
12. Debug with `references/testing-debugging.md` if needed.
13. Run `references/qa-checklist.md`.
14. For complex work, score `evals/evaluation-rubric.md` and correct hard failures.

### Implementation completion report

Report:
- tier selected for each target;
- APIs/renderer used;
- files/components changed;
- fallbacks and trigger conditions;
- reduced-motion/transparency/high-contrast behavior;
- performance strategy;
- tested/untested target matrix;
- known renderer limitations.

## 14. Design procedure

1. Map content and functional layers.
2. Remove unnecessary glass candidates.
3. Choose semantic variants: `regular`, `clear/media`, `prominent/tinted`, `frost`, `opaque`.
4. Define geometry, concentricity, grouping and spacing.
5. Define light/dark/backdrop adaptation.
6. Define interaction and reduced-motion behavior.
7. Define responsive/window-size behavior.
8. Produce implementation-ready tokens/components, not aesthetic adjectives only.
9. Audit with `references/qa-checklist.md`.

## 15. Audit/refactor procedure

Prioritize, in order:

1. hierarchy/overuse;
2. semantics/legibility;
3. native platform opportunities;
4. optical correctness;
5. geometry/concentricity/grouping;
6. compatibility/fallback accuracy;
7. interaction/motion;
8. performance/resource lifecycle;
9. maintainability and token/component reuse.

Return concrete fixes and explain whether each issue is design, rendering, accessibility, compatibility or performance.

## 16. Semantic token model

Prefer semantic tokens over raw optical knobs exposed everywhere:

- `glass.variant.regular|clear|prominent|frost|opaque`
- `glass.quality.full|balanced|fallback`
- `glass.radius.control|panel`
- `glass.diffusion.compact|panel`
- `glass.refraction.edge`
- `glass.dispersion`
- `glass.tint.neutral|prominent`
- `glass.rim.specular`
- `glass.edge.separation`
- `glass.shadow.compact|panel`
- `glass.motion.press|morph`

Keep low-level numbers private to the renderer/theme where possible. Tune against real content and hardware. Never imply values are official Apple constants unless Apple documents them.

## 17. Required final audit

Before declaring a task complete, run `references/qa-checklist.md`. A result is not complete if it has known dangling references, unsupported renderer claims, missing accessibility fallback, distorted semantic foreground, or unbounded performance cost.
