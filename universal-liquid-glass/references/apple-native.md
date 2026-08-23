# Apple-native Liquid Glass

Use this reference for SwiftUI, UIKit, AppKit, iOS/iPadOS/macOS/watchOS/tvOS, and when a cross-platform framework can bridge to native Apple glass.

## Core principle

Prefer system components before custom glass. On current Apple platforms, standard navigation, toolbar, search, tab, menu, popover, alert, sidebar, and many control surfaces automatically adopt the current Liquid Glass appearance when built with current SDKs. Do not manually add a raw glass effect on top of a system control that already receives the correct treatment.

Apple's design intent is hierarchical: Liquid Glass is a functional layer floating over content. Content-layer surfaces generally use standard materials. Glass should remain sparse enough that the underlying content is still the visual focus.

## Version strategy

- Treat the platform appearance as system-owned and version-adaptive. Avoid freezing a recreation of one beta/release's numeric blur, tint, shadow, or refraction values.
- Build with the current SDK and test the current OS first. Apple continues to refine the material across OS releases; apps using system components often inherit these changes automatically.
- If supporting pre-Liquid-Glass OS versions, keep behavior and semantics identical and allow the system to render the older material rather than attempting to back-port the newest look with fragile private APIs.
- Never use private frameworks, undocumented selectors, screenshots of system glass, or reverse-engineered private shaders in production guidance.

## SwiftUI

### Prefer system controls

Use `NavigationStack`, `NavigationSplitView`, `TabView`, toolbars, search, menus, popovers, system buttons, sheets, and other standard components before custom effects. In current SDKs these are designed to participate in the platform's visual hierarchy and transitions.

### Custom glass

Use `glassEffect(_:in:)` when a genuinely custom top-level functional element needs glass.

```swift
Text("Filter")
    .font(.headline)
    .padding(.horizontal, 16)
    .padding(.vertical, 10)
    .glassEffect(.regular.interactive(), in: .capsule)
```

Rules:

- `.regular` is the default and preferred general-purpose variant.
- `.clear` is for compact controls over visually rich backgrounds where revealing content is important and legibility remains safe. Do not mix regular and clear casually in one control group.
- Use `.tint(...)` only for semantic prominence, selection, or a primary action.
- Use `.interactive()` only on interactive custom surfaces.
- Apply `glassEffect` after modifiers that establish the view's intended appearance and bounds.
- Prefer `buttonStyle(.glass)` / prominent glass button styles for buttons instead of placing a button on an arbitrary raw glass plate.
- Keep labels/icons as semantic foreground content; the system owns the material behind/around them.

### Grouping and morphing

Use `GlassEffectContainer` for nearby glass shapes that should sample/render coherently and potentially merge or morph. Use stable glass IDs/transitions when animating related shapes. Do not imitate morphing by cross-fading unrelated blurry rectangles.

```swift
GlassEffectContainer(spacing: 12) {
    HStack(spacing: 12) {
        Button("Back") { }
            .buttonStyle(.glass)
        Button("Done") { }
            .buttonStyle(.glassProminent)
    }
}
```

Grouping is not merely decorative; it can improve rendering coherence and performance.

### Layout and scroll edges

- Prefer edge-to-edge content with functional glass floating above it when the information architecture supports that pattern.
- Use current scroll-edge APIs and system navigation behavior for legibility rather than adding opaque bands behind glass.
- Use adaptive layouts/size classes instead of device-model checks.
- Preserve concentricity near window/device corners. Let current platform geometry APIs solve this where available.

## UIKit

Prefer refreshed UIKit components first. For custom surfaces:

- `UIGlassEffect` provides glass material through `UIVisualEffectView`.
- `UIGlassContainerEffect` combines multiple glass elements and exposes grouping spacing.
- Use the effect's interactive/tint APIs rather than layering gesture-driven blur hacks.
- Keep `UIVisualEffectView` content in `contentView` and avoid bypassing its hierarchy.
- Do not apply both a custom glass effect and a system bar's built-in material to the same visual region.

When multiple nearby custom glass views need to behave as one visual family, use a container effect rather than independently sampling each surface.

## AppKit

Prefer system toolbars, sidebars, inspectors, search and controls. For custom top-level glass use current AppKit glass APIs such as `NSGlassEffectView` and container/grouping APIs where available in the deployment target.

On resizable Mac windows:

- test arbitrary window sizes;
- maintain concentricity with the enclosing window/container;
- keep toolbar groups semantically meaningful;
- avoid glass panels floating inside content merely for decoration;
- verify active/inactive window states.

## Interaction

Apple's material responds to direct manipulation, but interaction should remain restrained.

Good:
- system-provided press/highlight behavior;
- short direct-touch response;
- related-shape morphs;
- subtle pointer response on pointer platforms.

Avoid:
- permanent wobble;
- excessive bounce on every surface;
- animating raw blur radius as the main interaction cue;
- moving hit targets while the user is attempting to activate them.

## Accessibility and user settings

System glass can change in response to user appearance/accessibility settings. Do not assume the visual output is fixed.

- Test Reduce Transparency, Increase Contrast, Reduce Motion, light/dark appearance, and current Liquid Glass appearance settings where exposed.
- Use semantic/system foreground colors over system material.
- Avoid manually forcing transparency that defeats accessibility adaptation.
- Preserve Dynamic Type and accessibility sizes; a glass control must grow/reflow rather than clip text.

## iOS 27 / 2027-generation guidance

Apple's 2027 OS releases refine Liquid Glass automatically for apps already using the system design. Do not encode a separate home-grown “iOS 27 shader” unless implementing a non-native emulation. Current Apple guidance emphasizes improved diffusion over complex content, stronger depth separation, brighter specular response, adaptive sizing, and continuing use of system controls.

When a current SDK introduces a dedicated control style/API, prefer that over a raw `glassEffect` modifier. For example, a glass button style is semantically better than a generic glass background on a button.

## Verification checklist

- System component used where possible.
- No duplicate/manual glass over a system-owned glass region.
- Custom glass exists only at the top functional layer.
- `regular` vs `clear` choice is justified.
- Grouped glass uses native container APIs when appropriate.
- Dynamic Type, contrast, Reduce Transparency and Reduce Motion verified.
- Light/dark and bright/dark backdrops verified.
- Minimum deployment target receives an intentional fallback.
- No private API or reverse-engineered Apple constants.
