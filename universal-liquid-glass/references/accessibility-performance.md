# Accessibility, legibility and performance

Use for every implementation. Liquid Glass is incomplete if it only looks correct in a static screenshot.

## Accessibility invariants

The material must never be required to understand or operate the interface.

Preserve:
- semantic roles and accessible names;
- reading/focus order;
- keyboard/gamepad/switch navigation where applicable;
- visible focus indicators;
- target sizes appropriate to the platform;
- text selection and link/input behavior on web;
- Dynamic Type/font scaling and localization;
- disabled/selected/error state through more than color/transparency alone.

Decorative optical layers must not be focusable or intercept pointer/touch input.

## Contrast and dynamic backdrops

A glass foreground can move across many backgrounds, so checking contrast against one screenshot is insufficient.

Test foreground content over:
- near-white and near-black;
- saturated red/green/blue;
- high-frequency texture;
- faces/photos;
- video/moving content;
- gradients passing behind the control.

When contrast becomes unreliable, prefer this order:
1. adaptive foreground/system semantic color;
2. locally increase material diffusion/opacity;
3. add a subtle localized dimming/luminance-control layer;
4. use a stronger regular variant instead of clear;
5. switch to opaque/high-contrast fallback.

Avoid heavy text shadows as the primary legibility mechanism.

## Reduced transparency / high contrast

On Apple platforms, allow native material to respond to accessibility/system appearance settings and avoid overriding it with fixed transparency.

On the web and cross-platform stacks, support an explicit high-legibility mode because reduced-transparency signals are not uniformly exposed across environments.

A high-legibility fallback should preserve geometry and hierarchy while replacing refraction/translucency with a mostly opaque semantic surface. The layout should not jump when switching modes.

## Reduced motion

When reduced motion is requested:
- disable continuous lens wobble/noise/parallax;
- remove unnecessary morphing/overshoot;
- keep immediate pressed/selected state feedback;
- preserve state transitions using short fades or direct changes where appropriate;
- do not disable essential progress or spatial orientation cues without replacement.

On web honor `prefers-reduced-motion`. On native platforms use the platform accessibility setting/API.

## Motion safety

Even without reduced motion:
- do not animate the entire backdrop due to pointer movement;
- avoid strong magnification under a moving cursor;
- avoid repetitive oscillation;
- keep target geometry stable during activation;
- use direct, short and interruptible responses.

## Text scaling and localization

Glass controls must support long labels and larger text. Prefer content-driven sizing/minimum sizes rather than fixed-height pills that clip at accessibility text sizes. Test languages with longer strings and right-to-left layout when applicable.

## Performance budget model

Think in terms of surfaces, sampled pixels, passes and update frequency.

Approximate cost grows with:
- total pixel area sampled;
- blur/sample radius;
- number of refraction samples;
- number of independent surfaces;
- internal render resolution/DPR;
- refresh rate;
- frequency of source/backdrop updates;
- extra offscreen/compositing passes.

A tiny 60x40 lens at 120 Hz can be cheaper than a full-width 4K blurred toolbar even if the tiny lens uses a more complex shader.

## Adaptive quality

Use a deterministic quality ladder:

**Full** — shape-aware refraction, controlled diffusion, subtle dispersion, dynamic specular, interaction.

**Balanced** — lower optical resolution, single refraction sample, reduced/no dispersion, simpler lighting.

**Frost** — bounded backdrop blur/tint/rim/shadow.

**Opaque** — no transparency; same semantic hierarchy and geometry.

Degrade secondary surfaces before the primary navigation/action surface.

## Caching and invalidation

Cache anything determined only by geometry or material configuration:
- displacement maps;
- SDF textures/meshes;
- shader programs/pipelines;
- static noise textures;
- rounded masks.

Regenerate/reallocate when:
- width/height/radius changes materially;
- quality tier changes;
- device scale changes enough to require a new buffer.

Do not regenerate geometry-dependent assets for translation-only motion.

## Render-loop policy

Continuous rendering is justified only while something visible changes: animated backdrop, touch/pointer response, transition or live capture.

Otherwise:
- stop/pause RAF/display-link/ticker;
- stop live capture when hidden/minimized;
- use event-driven updates;
- release resources on unmount/dispose/context loss where appropriate.

## Scrolling

Avoid expensive glass inside repeated list rows. Prefer a fixed top-level glass navigation/control layer over scrolling content. If a repeated material is required, use a lower tier and profile realistic list length and fast fling/scroll.

## Memory and bandwidth

- Reuse textures/framebuffers.
- Avoid full-resolution CPU screenshots per frame.
- Avoid base64 frame transport in live desktop capture.
- Share scene textures across lenses.
- Cap internal render scale independent of display DPR where visual quality allows.
- Avoid retaining old generated SVG data URLs/maps after resize.

## Browser compositor pitfalls

Backdrop roots, filters, opacity, masks and transforms can create extra compositing layers and change what is sampled. Do not add `will-change` indiscriminately. Inspect performance/compositor tools when a design unexpectedly becomes expensive.

## Testing performance

Measure release/production builds on minimum hardware. Include:
- idle power/CPU/GPU;
- scrolling with maximum expected simultaneous lenses;
- resize/orientation;
- rapid navigation transitions;
- 60/90/120 Hz when applicable;
- thermal throttling for persistent effects;
- battery saver/low power behavior when relevant.

## Completion rule

If accessibility or minimum-device performance cannot be demonstrated, report the limitation and ship an explicit fallback rather than declaring the high-fidelity tier universally supported.
