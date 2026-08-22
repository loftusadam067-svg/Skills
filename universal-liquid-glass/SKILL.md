---
name: universal-liquid-glass
description: Design, implement, audit, or refactor high-fidelity Apple-style Liquid Glass interfaces across SwiftUI/UIKit/AppKit, HTML/CSS/JS, React/Next.js, Vue/Nuxt, Svelte, Angular, Astro, React Native/Expo, Flutter, Android/Compose, Electron/Tauri, Qt/QML, .NET and other frontend stacks. Use for Liquid Glass, iOS 26/27-style glass, refractive/frosted glass, glass navigation/toolbars/tab bars/controls, shader displacement/refraction, or converting an existing UI to Liquid Glass while preserving accessibility and performance.
license: MIT
compatibility: Kimi Agent, Kimi Code, and Agent Skills-compatible coding agents. Some implementations require platform/browser feature detection or native build tooling.
metadata:
  version: "2.0.0"
  research-date: "2026-08-23"
---

# Universal Liquid Glass

Build **Liquid Glass as a functional, adaptive material system**, not generic glassmorphism. Match Apple's design intent where possible, but never claim an emulation is Apple's native material.

## First: classify the task

Determine whether the user wants design, implementation, or audit/refactor. Before coding identify target framework/language and renderer; target OS/browser versions; native vs cross-platform requirements; dependency restrictions; minimum device/performance budget; light/dark themes and accessibility expectations; and whether the UI is content-heavy, media-heavy, or control-heavy. Preserve existing architecture, design tokens, state, routing, semantics, and component conventions unless there is a clear reason not to.

## Non-negotiable design model

Treat the interface as two layers: **content layer** (actual content, brand, data, media, reading surfaces, lists, tables, cards) and **functional layer** (controls/navigation floating above content). Use Liquid Glass primarily on the functional layer: navigation bars, tab bars, toolbars, search, floating actions, menus, popovers, segmented/toggle controls, transient controls, and controls over media. Do not make every card/panel/background glass. Read `references/design-system.md`.

## Fidelity ladder

Choose the highest viable tier and state it when implementing.

**Tier A — Native system Liquid Glass:** Apple platforms use system components/native APIs; cross-platform wrappers use verified native bridges when appropriate.

**Tier B — True refractive renderer:** Metal/AGSL/SkSL/GLSL/WebGL/WebGPU/canvas or equivalent scene-texture sampling.

**Tier C — Cross-browser/content refraction:** displacement map over rendered content/scene rather than Chromium-only SVG backdrop URL filters; preserve crisp semantics.

**Tier D — Direct backdrop SVG refraction:** `backdrop-filter: url(#...)` only after verifying the target browser matrix.

**Tier E — Frosted fallback:** backdrop blur + adaptive tint + restrained saturation/brightness + specular rim + depth shadow. This is not true refraction.

**Tier F — Opaque/high-contrast fallback:** for reduced transparency, unsupported hardware, accessibility, or severe performance constraints.

Never distort foreground text/icons to fake refraction.

## Material anatomy

Separate: backdrop/scene sampling; edge refraction strongest near rim with calm center; controlled diffusion/frost; adaptive luminosity/tint; coherent specular response; restrained depth separation; crisp foreground; subtle interaction response; and accessibility adaptation. Read `references/optics-and-rendering.md` and `references/web.md`.

## Apple-native rule

On current Apple platforms use system controls first. For custom SwiftUI glass use `glassEffect(_:in:)`; `.regular` by default; `.clear` only over visually rich safe backdrops; `.tint(...)` sparingly; `.interactive()` for genuinely interactive custom glass; `GlassEffectContainer` for nearby shapes that render/morph together; and glass button styles for actual buttons. UIKit should prefer `UIGlassEffect`/`UIVisualEffectView` and grouped APIs where available. Never hard-code reverse-engineered “Apple constants”. Read `references/apple-native.md`.

## Web rule

Do not equate `backdrop-filter: blur(...)` with true Liquid Glass. For high fidelity use shape-aware displacement/shaders, neutral interior, geometry-derived edge normals, optional tiny RGB sampling offset near rim, crisp foreground, feature detection, and deliberate frost fallback. With SVG `feDisplacementMap`, understand filter color space; when maps use neutral mid-gray byte encoding, use `color-interpolation-filters="sRGB"` if that matches the encoding. Never assume SVG-in-backdrop behavior is portable. Read `references/web.md`.

## Cross-platform rule

React Native/Expo/Capacitor: `references/react-native.md`; Flutter: `references/flutter.md`; Android/Compose: `references/android.md`; Electron/Tauri/Qt/.NET/desktop webviews: `references/desktop-hybrid.md`. If there is no Apple-native material, call the result an **emulation**.

## Accessibility

Preserve semantic roles, labels, reading order, keyboard navigation and focus indicators. Never encode meaning only through tint/transparency/refraction. Meet contrast targets over bright/dark moving backdrops. Respect reduced motion and reduced transparency/high contrast. Keep target-appropriate touch sizes. Preserve text selection/hit testing on web and ensure optical layers never steal events. `prefers-reduced-transparency` has limited browser support, so provide an app/manual high-legibility path when needed. Read `references/accessibility-performance.md`.

## Performance

Prefer native compositor paths. Limit simultaneous expensive refractive surfaces; cache displacement maps/shaders; never regenerate maps for position-only motion; update on geometry/quality changes; avoid fullscreen high-radius backdrop filters by default; reuse scene textures/backdrop captures; park/reduce render loops when static; profile minimum hardware; use adaptive quality. Degrade by removing secondary animation, reducing dispersion/refraction samples, lowering map/shader resolution/blur cost, converting secondary surfaces to frost-only, then opaque fallback.

## Motion and interaction

Use brief precise press responses, subtle direct-touch deformation, restrained pointer response, geometry morphs only between related controls/states, interruptible transitions, and reduced-motion alternatives. Avoid idle wobble, exaggerated jello, universal cursor magnetism, continuous noise animation, and layout-changing target instability.

## Implementation procedure

1. Inspect project and target matrix.
2. Classify candidate surfaces as content vs functional.
3. Choose fidelity tier per platform.
4. Define semantic tokens/variants.
5. Implement one reusable material primitive/modifier/component.
6. Keep optics separate from foreground semantics.
7. Add compatibility/accessibility fallbacks.
8. Integrate existing component/state/theme systems.
9. Profile expensive paths.
10. Run `references/qa-checklist.md`.
11. Report tiers, changed files/components, fallbacks, accessibility behavior, renderer limitations, and verification matrix.

## Design procedure

Map content/functional layers; minimize glass surfaces; choose semantic variants (`regular`, `clear/media`, `prominent/tinted`, `compact`, `panel`); define geometry/concentricity/spacing; light/dark/backdrop adaptation; interaction/reduced motion; implementation-ready token table; then audit with `references/qa-checklist.md`.

## Audit procedure

Prioritize hierarchy/overuse, foreground legibility, optical correctness, geometry/concentricity, interaction/motion, accessibility, performance, platform-native opportunities, and compatibility/fallbacks. Return concrete fixes.

## Semantic tokens

Prefer tokens such as `glass.variant.regular`, `glass.variant.clear`, `glass.variant.prominent`, `glass.blur.compact`, `glass.blur.panel`, `glass.diffusion`, `glass.refraction.edge`, `glass.dispersion`, `glass.tint.neutral`, `glass.tint.prominent`, `glass.rim.specular`, `glass.edge.separation`, `glass.shadow.compact`, `glass.shadow.panel`, `glass.radius.control`, `glass.radius.panel`, `glass.motion.press`, `glass.motion.morph`, and `glass.quality.full|balanced|fallback`. Tune values against actual content/hardware; do not imply numeric values are official Apple constants unless Apple documents them.

## Required final audit

Before declaring a Liquid Glass task complete, apply `references/qa-checklist.md`. For complex implementation work also use `evals/evaluation-rubric.md`.
