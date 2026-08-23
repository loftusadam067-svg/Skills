# Trigger and behavior test cases

Use these prompts to test whether the skill triggers appropriately and follows the right route. The expected behavior is more important than exact wording.

## Should strongly trigger

1. **"Make this iOS app use Liquid Glass properly."**
   - Inspect SwiftUI/UIKit/project target first.
   - Prefer current system components/native APIs.
   - Read `apple-native.md`, `design-system.md`, `accessibility-performance.md`, then QA.

2. **"Build an iOS 26 style refractive navbar in React."**
   - Read `web.md` and optics.
   - Do not promise native Apple material.
   - Choose shader/content-refraction or frost based on browser requirements.

3. **"Audit my website for fake AI glassmorphism and make it feel like Apple Liquid Glass."**
   - Run hierarchy/anti-slop audit before code.
   - Separate content vs functional layer.
   - Use `design-system.md`, `web.md`, QA and rubric.

4. **"Use /universal-liquid-glass to add glass tabs to my Expo app."**
   - Explicit invocation.
   - Inspect Expo SDK/Router versions.
   - Prefer native tabs / `expo-glass-effect` when supported; do not double-glass system UI.

5. **"Create a Flutter control that bends the image behind it like a lens."**
   - Read `flutter.md` + optics.
   - Distinguish native Apple bridge vs shader emulation.

6. **"Make this Compose toolbar look like Liquid Glass."**
   - Read `android.md` + design/accessibility.
   - Call it an emulation and choose AGSL/blur fallback based on API target.

7. **"My Electron transparent window should refract the actual desktop."**
   - Read `desktop-hybrid.md`.
   - Explain host-provided capture/wallpaper source requirement and privacy/fallbacks.

8. **"The SVG glass filter shifts everything up and left."**
   - Read `web.md`, optics and debugging guidance.
   - Check displacement-map midpoint/channel/color-space mismatch before redesigning.

9. **"Liquid glass looks fine but scrolling drops to 30 fps."**
   - Read accessibility/performance and platform renderer reference.
   - Profile sampled area, surface count, buffer DPR, blur/sample count and invalidation.

10. **"Redesign these cards with Apple glass."**
    - Trigger, but challenge the assumption: cards are content-layer by default.
    - Keep most cards non-glass and use glass on functional controls unless the product context clearly justifies otherwise.

## Should trigger lightly / only when relevant

11. **"Make the header translucent."**
    - If no Liquid Glass/iOS/refraction intent, normal frontend guidance may be enough. Do not force advanced shader optics.

12. **"Use a frosted blur behind this modal."**
    - Can use the skill if the design context is Liquid Glass-like, but call it frost unless refraction exists.

13. **"How does feDisplacementMap work?"**
    - General SVG explanation is sufficient unless the user connects it to glass UI.

## Should not hijack unrelated design tasks

14. **"Design a brutalist portfolio."**
    - Do not inject Liquid Glass unless asked.

15. **"Make this dashboard accessible."**
    - Accessibility skill/general guidance should lead unless glass/transparency is central.

16. **"Create a React button."**
    - Do not add glass by default.

17. **"Explain refraction in physics."**
    - This is a physics question, not a UI material task.

## Regression expectations

For every strong-trigger implementation response, verify:
- the target renderer is identified before selecting a tier;
- native Apple APIs are preferred on supported Apple-native projects;
- non-Apple implementations are called emulations;
- blur-only fallback is not called true refraction;
- semantic foreground is never distorted;
- fallback/accessibility strategy is present;
- QA checklist is used before completion.
