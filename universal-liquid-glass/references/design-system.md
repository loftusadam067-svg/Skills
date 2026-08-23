# Liquid Glass design system

Treat Liquid Glass as a **functional layer** floating above a **content layer**. The material should clarify hierarchy and reveal content, not become the content.

## Surface classification

### Strong glass candidates
- primary navigation/tab bars;
- toolbars and grouped top-level actions;
- search/navigation affordances;
- floating primary/secondary actions;
- popovers, menus and transient contextual controls;
- media controls over imagery/video;
- transient sliders/toggles/selection lenses;
- compact controls that genuinely benefit from seeing the content beneath.

### Usually not glass
- article/body backgrounds;
- every content card;
- dense data tables;
- long reading surfaces;
- large static dashboard sections;
- decorative panels with no interactive/hierarchical role;
- nested containers already sitting inside another glass region.

A user request for “glass cards” is not automatically a good hierarchy decision. Consider using standard material for the cards and glass for their controls.

## Semantic variants

### Regular
Default for most functional surfaces, complex backdrops, meaningful text and larger glass regions. Prioritize legibility and adaptation.

### Clear / media
Use selectively when preserving visually rich media is the point, the control is compact, contrast is demonstrably safe and a dimming/legibility mechanism is available. Clear glass should not become a low-contrast default.

### Prominent / tinted
Reserve for primary action, selected state or meaningful semantic emphasis. Tint should communicate function, not decorate every control. Do not colorize an entire toolbar merely to make it “interesting.”

### Frost
A non-refractive fallback for platforms where true/native refraction is unavailable or too expensive. Keep the same hierarchy/geometry.

### Opaque
High-legibility/accessibility/performance fallback. Preserve shape, spacing and state so switching mode does not reorganize the UI.

Do not casually mix materially different variants within one tightly related control group.

## Geometry and concentricity

- Compact controls: capsule, circle, or continuous rounded shape.
- Larger functional surfaces: continuous rounded rectangles with radii proportional to size and context.
- Nested corner geometry should appear concentric with the containing window/panel. Inner radius should relate to outer radius and inset rather than being arbitrary.
- Nearby related glass shapes should use platform grouping/container behavior when available.
- Avoid stacks of unrelated rounded rectangles and excessive “pillification.”

On resizable layouts, derive geometry from container/size classes/breakpoints rather than hard-coded device models.

## Edge-to-edge and scroll relationship

Glass is most convincing when meaningful content can move beneath it.

Prefer:
- edge-to-edge content where appropriate;
- floating navigation/control surfaces rather than opaque bars;
- platform scroll-edge legibility effects;
- controls that remain spatially stable while content moves behind them.

Avoid decorative glass strips over empty backgrounds or placing a huge translucent panel over content only to restore readability with an opaque tint.

## Color and adaptation

Native Liquid Glass is environment-adaptive rather than a fixed RGBA recipe. Emulations should preserve that principle:

- keep neutral glass mostly neutral;
- sample/estimate backdrop luminance when practical;
- adjust diffusion/tint/foreground before adding heavy shadows;
- use semantic/system foreground colors;
- test bright, dark, saturated, patterned and moving backgrounds;
- give larger/thicker surfaces more diffusion and depth separation than tiny controls;
- avoid fixed white tint as a universal solution.

Current Apple refinements emphasize stronger diffusion over complex content, clearer edge separation and brighter specular response while retaining content-first hierarchy. Treat these as design cues, not numeric constants.

## Lighting and depth

A believable material has a coherent light model:

- directional specular rim/sheen;
- subtle darker edge/depth separation;
- broad restrained ambient shadow;
- stronger depth/diffusion for larger or visually thicker glass;
- nearby environmental color spill only when it remains subtle and contextually plausible.

A uniform 1px white border is not an optical model. Neon/rainbow outlines are not a substitute for refraction.

## Typography and iconography

- Keep labels/icons crisp and outside the refraction/blur pass.
- Prefer semantic/system iconography where it fits the product.
- Avoid ultra-thin low-contrast type over moving imagery.
- Let controls grow/reflow for text scaling and localization.
- Do not use text shadow to compensate for an incorrectly transparent material.

## Grouping and prominence

Group controls by function, not merely visual proximity. One glass group can communicate a related tool cluster; a primary action may use a separate prominent/tinted treatment. Over-grouping every toolbar item into one long capsule destroys hierarchy.

## Motion

Use motion to reinforce direct manipulation:
- short tactile press response;
- subtle pointer highlight on pointer platforms;
- geometry morph between clearly related states;
- smooth, interruptible transitions;
- material depth/refraction that changes modestly as a surface grows/shrinks.

Avoid:
- idle wobble;
- permanent liquid noise;
- universal jelly physics;
- long bounce chains;
- giant parallax;
- moving controls away from the pointer/finger during activation;
- animation required to understand state.

## Responsive / multi-input behavior

Test:
- phone portrait/landscape;
- tablet split view/resizable windows;
- desktop arbitrary window sizes;
- touch, pointer, keyboard and focus navigation;
- safe areas/cutouts;
- large text and localization.

Use semantic layout adaptation rather than device-name checks.

## Anti-slop rules

Reject or revise:
- hero + three glass cards + giant glass CTA as a default AI layout;
- glass on every container;
- enormous blur values doing all visual work;
- oversized radii everywhere;
- fixed white translucent cards regardless of background;
- neon/rainbow edges;
- random RGB fringing;
- thin illegible text over photography;
- multiple glass layers sampling one another;
- decorative glass with no hierarchy/function;
- giant static glass panels hiding the content they are supposed to reveal;
- cursor-following distortion applied to the whole page.

## Semantic tokens

Expose intent-level tokens/components:

```text
glass.variant.regular | clear | prominent | frost | opaque
glass.quality.full | balanced | fallback
glass.radius.control | panel
glass.diffusion.compact | panel
glass.refraction.edge
glass.dispersion
glass.tint.neutral | prominent
glass.rim.specular
glass.edge.separation
glass.shadow.compact | panel
glass.motion.press | morph
```

Keep renderer-specific sample counts, blur radii, shader scales and displacement-map internals private to the platform/theme when possible.

## Design acceptance test

A design is not ready if removing the glass effect destroys its hierarchy. The underlying layout, typography, grouping and semantics must already make sense; Liquid Glass should enhance that structure rather than create it from nothing.
