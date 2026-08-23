# Universal Liquid Glass

A cross-platform Agent Skill for designing, implementing, auditing and refactoring high-fidelity **Liquid Glass** interfaces without collapsing the concept into generic glassmorphism.

The skill prefers native Apple Liquid Glass where available and chooses an explicit emulation/fallback tier elsewhere. It covers SwiftUI, UIKit, AppKit, web frameworks, React Native/Expo, Flutter, Android/Compose, Electron/Tauri, Qt/QML, .NET and other frontend renderers.

## What makes it different

- **Hierarchy first:** glass is primarily a functional/navigation layer above content.
- **Native first:** standard Apple controls and public system glass APIs take priority over recreations.
- **Optically explicit:** true refraction, content refraction, SVG-backdrop refraction, frost and opaque fallback are distinct tiers.
- **Cross-platform:** one semantic design model with renderer-specific implementation guidance.
- **Accessibility/performance are mandatory:** high-legibility fallbacks, reduced motion, bounded effects, caching and adaptive quality are part of the workflow.
- **Progressive disclosure:** core instructions stay in `SKILL.md`; detailed platform guidance lives in `references/`.
- **Validated packaging:** `scripts/validate_skill.py` fails on missing required files and dangling references.
- **Evaluated behavior:** `evals/` contains trigger/regression cases and a scored implementation rubric.

## Structure

```text
universal-liquid-glass/
├── SKILL.md
├── README.md
├── KIMI_INSTALL_PROMPT.md
├── LICENSE
├── CHANGELOG.md
├── references/
│   ├── design-system.md
│   ├── optics-and-rendering.md
│   ├── apple-native.md
│   ├── web.md
│   ├── react-native.md
│   ├── flutter.md
│   ├── android.md
│   ├── desktop-hybrid.md
│   ├── accessibility-performance.md
│   ├── testing-debugging.md
│   ├── qa-checklist.md
│   └── sources.md
├── evals/
│   ├── evaluation-rubric.md
│   └── trigger-cases.md
└── scripts/
    └── validate_skill.py
```

## Kimi installation

Open Kimi Agent mode, invoke `/skill-creator`, and use the prompt in [`KIMI_INSTALL_PROMPT.md`](KIMI_INSTALL_PROMPT.md). The prompt tells Kimi to import the whole skill directory, verify the required files, and preserve progressive disclosure rather than flattening the package unless its environment requires it.

Repository skill URL:

`https://github.com/loftusadam067-svg/Skills/tree/main/universal-liquid-glass`

## Other Agent Skills-compatible agents

Agents that support directory-form Agent Skills can install/copy the `universal-liquid-glass` folder into their normal skills directory. Where the `skills` CLI is supported, the repository can be installed and the skill selected by name.

Always follow the target agent's current installation documentation; scan directories and CLI flags differ by product.

## Validate

From the repository root:

```bash
python universal-liquid-glass/scripts/validate_skill.py
```

The validator is stdlib-only and checks:
- required package files;
- `SKILL.md` frontmatter basics;
- the Agent Skills progressive-disclosure line guideline;
- explicit internal paths referenced by `SKILL.md`;
- unresolved placeholders;
- empty/non-UTF-8 markdown files.

## Research policy

The skill is grounded first in current Apple/standards/framework documentation and then uses maintained public implementations for engineering techniques. See [`references/sources.md`](references/sources.md).

Package/API versions are deliberately not hard-coded as permanent recommendations. Agents should inspect the user's actual project and current first-party documentation before dependency-specific implementation.

## License

MIT. See [`LICENSE`](LICENSE).
