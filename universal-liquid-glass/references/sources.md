# Research sources and evidence policy

Research baseline: 2026-08-23. This file records the primary standards/docs and representative public implementations used to refine the skill. It is not a lockfile: package versions and platform APIs must be re-verified when implementing.

## Source priority

When sources conflict, use this order:

1. Current first-party platform/framework documentation and Human Interface Guidelines.
2. Current standards/specifications and browser documentation.
3. Maintained official framework skills/examples.
4. Maintained open-source implementations with inspectable code.
5. Community articles/demos as implementation ideas, never as official constants.

Never treat reverse-engineered numeric values as Apple-defined material parameters unless Apple documents them.

## Apple primary sources

- Liquid Glass technology overview: https://developer.apple.com/documentation/technologyoverviews/liquid-glass
- Adopting Liquid Glass: https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
- HIG Materials / Liquid Glass: https://developer.apple.com/design/human-interface-guidelines/materials
- Applying Liquid Glass to custom SwiftUI views: https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views
- `glassEffect(_:in:)`: https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)
- `GlassEffectContainer`: https://developer.apple.com/documentation/swiftui/glasseffectcontainer
- `Glass`: https://developer.apple.com/documentation/swiftui/glass
- `UIGlassEffect`: https://developer.apple.com/documentation/uikit/uiglasseffect
- `UIGlassContainerEffect`: https://developer.apple.com/documentation/uikit/uiglasscontainereffect
- WWDC25 Meet Liquid Glass: https://developer.apple.com/videos/play/wwdc2025/219/
- WWDC25 What's new in UIKit: https://developer.apple.com/videos/play/wwdc2025/243/
- WWDC25 Build an AppKit app with the new design: https://developer.apple.com/videos/play/wwdc2025/310/
- WWDC26 What's new in SwiftUI: https://developer.apple.com/videos/play/wwdc2026/269/
- WWDC26 Design guide: https://developer.apple.com/wwdc26/guides/design/

Key evidence reflected by the skill: Liquid Glass is primarily a functional layer for controls/navigation; standard components should be preferred; regular vs clear have distinct roles; system material adapts to backdrop/settings; larger/thicker glass uses stronger depth/diffusion cues; current system frameworks continue to refine the appearance across releases.

## Agent Skills / Kimi

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills best practices: https://agentskills.io/skill-creation/best-practices
- Kimi Agent Skills documentation: https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html
- Kimi Help — What are Skills?: https://www.kimi.com/en/help/features/what-are-skills
- Kimi Help — Use Skills in Agent Mode: https://www.kimi.com/en/help/features/use-skills-in-agent

This package follows progressive disclosure: concise trigger/core workflow in `SKILL.md`, detailed material in `references/`, executable validation in `scripts/`, and evaluation prompts/rubric in `evals/`.

## Web standards and browser references

- MDN `backdrop-filter`: https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter
- MDN `feDisplacementMap`: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap
- MDN SVG `<filter>`: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter
- MDN CSS filter effects: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects/Using

Important distinction: generic SVG filter primitive support is not proof that every browser supports the same SVG URL filter behavior through `backdrop-filter`. Verify the exact rendering path.

## Cross-browser optical implementation reference

- Aave Design — Building Glass for the Web: https://aave.com/design/building-glass-for-the-web

Useful engineering idea: the displacement map can be portable across renderers. SVG can drive DOM/content filtering while WebGL can use the same conceptual map when a scene texture must be sampled. Treat the article's implementation as evidence/technique, not an Apple specification.

## Expo / React Native

- Expo GlassEffect: https://docs.expo.dev/versions/latest/sdk/glass-effect/
- Expo BlurView: https://docs.expo.dev/versions/latest/sdk/blur-view/
- Expo Router native tabs: https://docs.expo.dev/router/advanced/native-tabs/
- Expo Router stack: https://docs.expo.dev/router/advanced/stack/
- Expo UI SwiftUI guide: https://docs.expo.dev/guides/expo-ui-swift-ui/
- Expo Skills for AI agents: https://docs.expo.dev/skills/

Representative open-source implementation:
- Callstack Liquid Glass for React Native: https://github.com/callstack/liquid-glass

Always verify current SDK/package requirements before recommending an install.

## Android / Compose

- Android RuntimeShader: https://developer.android.com/reference/android/graphics/RuntimeShader
- Using AGSL: https://developer.android.com/develop/ui/views/graphics/agsl/using-agsl
- Compose shaders/Brush: https://developer.android.com/develop/ui/compose/graphics/draw/brush

Representative implementation:
- Kyant AndroidLiquidGlass: https://github.com/Kyant0/AndroidLiquidGlass

## Flutter

- Flutter `dart:ui`: https://api.flutter.dev/flutter/dart-ui/
- Flutter `BackdropFilter`: https://api.flutter.dev/flutter/widgets/BackdropFilter-class.html
- Flutter fragment programs/shaders: consult current Flutter `dart:ui`/shader documentation for the shipping SDK.

Representative community implementations to inspect, not blindly install:
- https://github.com/whynotmake-it/flutter_liquid_glass
- https://github.com/sdegenaar/liquid_glass_widgets
- https://github.com/kiddo4/real_liquid_glass

## Public open-source web/agent implementations reviewed

Representative projects:
- https://github.com/deepika-builds/liquid-glass
- https://github.com/archisvaze/liquid-glass
- https://github.com/dashersw/liquid-glass-js
- https://github.com/rdev/liquid-glass-react
- https://github.com/Na2H2P2O7/liquid-glass-skill
- https://github.com/GetStream/awesome-liquid-glass
- https://github.com/xinlingfeiwu/liquid-glass-design-skill

Lessons retained only when they agree with platform/standards evidence or are clearly labeled implementation strategies: edge-focused displacement, neutral center, subtle chromatic separation, shared scene textures, render-loop parking, adaptive quality, and crisp semantic foreground content.

## Freshness rule for agents

Before giving dependency/version-specific code:

1. inspect the project's actual versions;
2. check current first-party docs/changelogs when web access exists;
3. prefer APIs supported by the user's minimum target;
4. state when an API is beta/preview/experimental;
5. avoid pinning a package version from this research file;
6. never infer support solely from a similar platform or older release.
