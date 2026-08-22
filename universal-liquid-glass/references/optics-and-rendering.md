# Optics and rendering

Portable pipeline: scene/backdrop → shape mask/signed distance → surface normal/displacement field → refracted samples → optional tiny chromatic separation → diffusion/blur → adaptive tint/luminosity → edge/specular lighting → depth composite → crisp foreground UI.

## Signed distance and edge field

For rounded shapes derive distance to boundary and use its gradient as an approximate 2D normal. Keep displacement near zero through the central plateau, rising smoothly through the bevel, peaking near the visually thick edge and decaying cleanly at the boundary. Unstructured turbulence must not be the primary normal field.

## Displacement maps

Encode X/Y displacement in known channels, use channel midpoint as neutral, keep most interior neutral, and strongest deviations at bevel. For SVG `feDisplacementMap`, filter color space changes channel interpretation. If authored for ordinary sRGB byte values, set `color-interpolation-filters="sRGB"`. Confirm x/y channel selectors rather than copying conventions blindly.

## Chromatic dispersion

Use tiny RGB refraction-strength differences near the rim, converging in the center, and disable in lower quality. If users notice rainbow fringe before glass, it is too strong.

## Diffusion

Blur represents scattering/legibility, not refraction. Prefer bounded/clipped blur, enough to stabilize contrast, less in small clear/media controls, more for large complex surfaces. Do not use giant blur radii as a substitute for optical structure.

## Specular response

Where possible derive highlight from geometry/normal and a coherent light direction, shape nonlinearly, and mask to bevel/rim. A coherent gradient sheen is an acceptable fallback.

## Scene sampling

Native system material: let OS own sampling. GPU renderer: render/capture scene texture and sample in shader. Web content-refraction: refract live rendered content or purpose-built inert copy. Direct backdrop filter: convenient only where verified. Desktop webviews cannot inherently sample other windows; host may need to supply wallpaper/screen/window texture and coordinates.

## Interaction

For press/touch subtly reshape bevel or modulate refraction/specular while keeping foreground target geometry stable. Drive shader parameters rather than recomputing full geometry when possible.

## Quality tiers

**Full:** scene refraction, shape-aware normals, subtle dispersion, diffusion, dynamic specular, interaction. **Balanced:** lower-resolution map/shader, single refraction sample, minimal/no dispersion, simplified specular. **Frost:** backdrop blur, adaptive tint, coherent rim/shadow, crisp foreground. **Opaque:** semantic high-contrast surface with same geometry/hierarchy.
