# Skills

Public AI-agent skills maintained by Adam Loftus.

## Universal Liquid Glass

[`universal-liquid-glass`](universal-liquid-glass/) is a cross-platform Agent Skill for designing, implementing, debugging, auditing and refactoring high-fidelity Apple-style Liquid Glass interfaces.

It covers:
- SwiftUI, UIKit and AppKit with native public Apple Liquid Glass APIs;
- HTML/CSS/JS and React/Next.js, Vue/Nuxt, Svelte/SvelteKit, Angular, Astro and Tailwind;
- React Native and Expo;
- Flutter;
- Android Views, Jetpack Compose and Compose Multiplatform;
- Electron, Tauri, pywebview, Qt/QML and .NET desktop/hybrid apps;
- accessibility, adaptive quality, performance, testing/debugging and fallback design.

The skill distinguishes native Liquid Glass, true GPU refraction, portable content refraction, verified SVG-backdrop refraction, frosted fallback and opaque/high-legibility fallback instead of calling every blurred surface “Liquid Glass”.

### Kimi

Open the skill's [`KIMI_INSTALL_PROMPT.md`](universal-liquid-glass/KIMI_INSTALL_PROMPT.md), invoke `/skill-creator` in Kimi Agent mode, and paste the install/update prompt.

### Validate

```bash
python universal-liquid-glass/scripts/validate_skill.py
```

GitHub Actions also validates the package on relevant pushes and pull requests so missing/dangling reference files cannot be silently reintroduced.
