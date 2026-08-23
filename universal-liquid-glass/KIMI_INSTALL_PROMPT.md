# Kimi install / update prompt

Paste the block below into Kimi Agent mode after invoking `/skill-creator`.

```text
Create or update my custom Kimi skill named `universal-liquid-glass` from this public GitHub directory:

https://github.com/loftusadam067-svg/Skills/tree/main/universal-liquid-glass

Treat the GitHub directory as the canonical source. Import the complete package, not only SKILL.md.

Required files that must exist before you consider the import successful:
- SKILL.md
- README.md
- LICENSE
- references/design-system.md
- references/optics-and-rendering.md
- references/apple-native.md
- references/web.md
- references/react-native.md
- references/flutter.md
- references/android.md
- references/desktop-hybrid.md
- references/accessibility-performance.md
- references/testing-debugging.md
- references/qa-checklist.md
- references/sources.md
- evals/evaluation-rubric.md
- evals/trigger-cases.md
- scripts/validate_skill.py

First inspect SKILL.md and verify that every path it references exists in the GitHub directory. Do not silently ignore a missing reference. If any required file is unavailable, report the exact missing paths and stop rather than installing a degraded skill.

Preserve the package's progressive-disclosure structure when your skill environment supports directory-form skills: SKILL.md is the core instructions, references/ contains on-demand platform guidance, evals/ contains quality/trigger tests, and scripts/ contains validation. Do not flatten everything into SKILL.md unless Kimi's active skill environment requires a single file. If flattening is required, preserve all rules and clearly label the merged sections.

Use the frontmatter name and description from SKILL.md so the skill auto-triggers for Liquid Glass, iOS/current Apple glass, refractive/frosted frontend UI, glass navigation/toolbars/tab bars/controls, shader/SVG displacement, cross-platform emulation, glass audits/debugging and performance/compatibility problems.

Preserve these non-negotiable behaviors:
1. classify the target framework/renderer/OS/browser before choosing a technique;
2. use Liquid Glass primarily on the functional/navigation layer, not every content card;
3. use the highest viable fidelity tier A-F and state it during implementations;
4. prefer native public Apple components/APIs on supported Apple platforms;
5. never call blur-only frost true refraction or native Apple Liquid Glass;
6. keep semantic foreground text/icons crisp and outside optical distortion;
7. choose renderer-specific strategies for web, Expo/RN, Flutter, Android and desktop instead of forcing one implementation everywhere;
8. preserve accessibility, reduced-motion/transparency/high-contrast fallbacks, semantics and responsive behavior;
9. enforce bounded effects, caching, cleanup, adaptive quality and render-loop parking;
10. verify current dependency/API documentation when version-specific guidance matters;
11. run references/qa-checklist.md before completion and evals/evaluation-rubric.md for complex implementations.

If you are updating an existing `universal-liquid-glass` skill, replace the old canonical instructions/references with this repository version rather than keeping conflicting obsolete copies. Preserve only user-specific customizations that do not contradict the new core rules.

After import, run or logically perform the checks in scripts/validate_skill.py if execution is unavailable. Confirm:
- no dangling SKILL.md references;
- all required files are present;
- SKILL.md frontmatter is intact;
- the installed skill can be invoked as `/universal-liquid-glass`;
- automatic triggering uses the SKILL.md description.

Then report the installed source URL, version from SKILL.md metadata, install location, whether the package remained directory-structured or was flattened, and validation result.
```
