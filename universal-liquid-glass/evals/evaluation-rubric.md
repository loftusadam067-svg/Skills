# Universal Liquid Glass evaluation rubric

Use this rubric for complex design/implementation/audit tasks. Score each section 0-4. A production-ready result should score at least 28/32 with **no zero** in hierarchy, accessibility, compatibility, or correctness.

## 1. Task/platform classification

**4** — Correctly identifies design vs implementation vs audit; framework, renderer, minimum OS/browser, native vs emulated path, dependency constraints and performance target are explicit.

**3** — Correct platform/fidelity choice with one minor missing constraint.

**2** — Broadly correct but assumes important compatibility details.

**1** — Chooses technology before understanding target matrix.

**0** — Uses an incompatible API or wrong platform entirely.

## 2. Hierarchy and Apple design intent

**4** — Glass is concentrated on functional/navigation surfaces; content remains primary; regular/clear/prominent variants are semantically justified; no unnecessary glass-on-glass nesting.

**3** — Mostly correct with minor overuse.

**2** — Several decorative content cards use glass without purpose.

**1** — Glass dominates the content layer.

**0** — Generic all-glass aesthetic contradicts the functional-layer model.

## 3. Optical/material correctness

**4** — Native material used where available, or emulation has explicit backdrop sampling, shape-aware edge refraction, calm center, controlled diffusion, adaptive tint, coherent specular/depth and crisp foreground.

**3** — Strong material with one missing optical cue.

**2** — High-quality frost but incorrectly described as refraction, or refraction is visually crude.

**1** — Blur + transparent white rectangle only.

**0** — Foreground text/icons are distorted or material breaks usability.

## 4. Geometry and interaction

**4** — Continuous/concentric geometry, correct grouping, stable hit targets, restrained direct manipulation, interruptible/reduced-motion behavior.

**3** — Good geometry with minor motion/spacing issues.

**2** — Inconsistent radii or over-animated interactions.

**1** — Arbitrary rounded rectangles/jello behavior.

**0** — Interaction changes targets/layout unpredictably.

## 5. Accessibility and legibility

**4** — Semantics/focus intact; dynamic backdrop contrast tested; reduced motion and transparency/high-contrast fallback implemented; text scaling/localization considered; state not encoded only by color/transparency.

**3** — All core accessibility behavior present with one minor gap.

**2** — Static contrast only or fallback incomplete.

**1** — Accessibility mentioned but not implemented/tested.

**0** — Glass makes content inaccessible or semantics are removed.

## 6. Performance/resource behavior

**4** — Effects bounded; buffers/maps/shaders shared/cached; translation doesn't regenerate geometry; render loop parks; quality ladder implemented; minimum hardware/profile strategy documented.

**3** — Efficient overall with one avoidable cost.

**2** — Works but uses redundant surfaces/passes or continuous rendering.

**1** — Obvious full-screen/heavy repeated effects without profiling.

**0** — Architecture is predictably unusable on target hardware.

## 7. Compatibility and fallback correctness

**4** — Exact feature path is verified; native vs emulated terminology accurate; fallback chain is deterministic; unsupported browsers/OS versions preserve function and layout.

**3** — Strong matrix with one unverified edge case.

**2** — Generic feature detection but fragile renderer assumptions remain.

**1** — Browser/OS support guessed from unrelated APIs.

**0** — No fallback or known unsupported path presented as universal.

## 8. Code/integration quality

**4** — Reusable semantic primitive; existing architecture/tokens/state preserved; cleanup/resources handled; dependency choices justified/current; verification steps provided.

**3** — Clean implementation with minor duplication.

**2** — Functional but invasive or poorly abstracted.

**1** — Large rewrite for a visual effect, unmaintainable magic numbers, or missing cleanup.

**0** — Broken/incomplete implementation.

## Hard-fail conditions

Regardless of numeric score, fail the result if any apply:

- claims a frost-only blur is true/native Liquid Glass;
- uses private/undocumented Apple APIs in production guidance;
- distorts semantic foreground text/icons for refraction;
- removes keyboard/screen-reader semantics;
- has no fallback for a known unsupported required platform;
- applies expensive refractive material to an unbounded repeated list/fullscreen layer without justification;
- leaves dangling file/reference paths in a delivered skill/package;
- recommends a current dependency/version without checking the current project/docs when verification is available.

## Expected completion report

A strong implementation ends with a concise matrix containing:

| Target | Tier | Renderer/API | Fallback | Accessibility | Verified |
|---|---|---|---|---|---|
| example | A/B/etc | native/shader/etc | frost/opaque | reduced motion/transparency | yes/needs device |

Also list remaining renderer limitations rather than concealing them.
