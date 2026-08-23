# React Native, Expo and Capacitor

Use for React Native, Expo Router/Expo UI, bare React Native, Capacitor, and hybrid mobile apps that can bridge to native platform effects.

## Default strategy

Treat iOS and Android separately at the rendering layer while keeping one semantic component API.

Recommended component contract:

```ts
type GlassVariant = 'regular' | 'clear' | 'prominent' | 'frost' | 'opaque';
type GlassQuality = 'auto' | 'full' | 'balanced' | 'fallback';
```

Expose semantic props; keep platform-specific optical parameters internal.

## Expo on iOS

Prefer current Expo-native support before third-party shader recreations.

Current Expo provides `expo-glass-effect`, whose `GlassView` uses native iOS visual-effect infrastructure on supported iOS versions. It falls back on unsupported platforms. Verify the installed Expo SDK documentation before coding because the API and platform behavior can evolve quickly.

Important known behavior from current Expo docs:
- native GlassView requires supported iOS versions;
- setting `opacity: 0` on GlassView or an ancestor can prevent the effect from rendering; use the component's supported animation path instead of fading the entire native view when possible;
- native navigation/tab components may already adopt system Liquid Glass, so do not add another custom glass layer behind them;
- match the app's theme to system light/dark state to avoid visual flashes during native navigation transitions.

Example shape only; verify exact current API names before use:

```tsx
import { GlassView } from 'expo-glass-effect';

<GlassView style={styles.control}>
  <Text>Action</Text>
</GlassView>
```

## Expo UI / SwiftUI bridge

If the project already uses Expo UI SwiftUI components, current Expo exposes SwiftUI modifiers including a glass effect on supported Xcode/iOS versions. Prefer that native path for Apple-only UI islands rather than reimplementing the optics in JavaScript.

## Expo Router

- Native iOS headers and tabs can adopt system Liquid Glass automatically on current iOS releases.
- Prefer native tabs when native look/behavior is the product goal.
- Do not obscure or double-wrap a native glass tab bar with a custom BlurView.
- Verify minimize-on-scroll and header behavior against the current Expo Router version.
- When visual artifacts appear on theme switches, verify ThemeProvider/light-dark synchronization before changing glass parameters.

## Bare React Native

Priority:
1. system/native component or maintained native bridge;
2. native view implemented through TurboModules/Fabric/Expo Modules if project architecture allows;
3. GPU/canvas/skia emulation where native material is unavailable;
4. blur/frost fallback.

When evaluating a third-party native glass package:
- confirm active maintenance and release date;
- confirm minimum Xcode/iOS/RN versions;
- confirm New Architecture compatibility;
- confirm Expo Go vs development-build requirements;
- inspect license;
- confirm whether it uses public native APIs;
- test unmount/remount, scrolling, opacity, transforms and nested views.

Do not copy a dependency recommendation from this skill without verifying its current release documentation.

## Android path

Do not label the Android result as native Apple Liquid Glass. Use an emulation based on Compose/Android shader or bounded blur capabilities; see `android.md`. Keep the same semantic component variants so the design hierarchy remains consistent across platforms.

## Capacitor

Capacitor's web content follows `web.md`. Native shells cannot magically make an arbitrary DOM element use Apple system glass.

Choose one of:
- web frost/refraction inside the WebView;
- a native plugin/view layered with careful coordinate and input synchronization;
- native navigation outside the WebView using platform material.

If using a native overlay, ensure safe-area, rotation, keyboard, scroll and hit-test synchronization. Avoid a visually perfect overlay that is semantically detached from the web control beneath it.

## Accessibility

- Keep React Native accessibility roles/labels on the semantic foreground component.
- Do not make the decorative native/shader layer independently focusable.
- Respect Reduce Motion and platform accessibility settings where exposed.
- Provide an explicit opaque/high-contrast fallback when transparency adaptation cannot guarantee readability.
- Test font scaling and long localized strings; glass shapes must resize rather than clip.

## Performance

- Avoid a BlurView/GlassView behind every list item.
- Keep expensive material surfaces outside virtualized scrolling rows when possible.
- Prefer one persistent navigation/control surface over many transient GPU layers.
- On Skia/shader implementations, share runtime effects and textures, cap render scale, and pause animations when the screen is unfocused.
- Profile release builds on a minimum target phone; development tooling distorts JS/GPU performance.

## Fallback component pattern

Build one abstraction that resolves the renderer:

```text
if iOS supports verified native glass:
    native glass
else if platform has verified GPU refraction path and quality allows:
    shader emulation
else if blur is available:
    frosted material
else:
    opaque semantic surface
```

The fallback must preserve spacing, corner geometry, target size, state, and interaction so the UI does not reflow dramatically between platforms.

## Verification

- iOS current + oldest supported iOS.
- Android minimum + representative modern device.
- Expo Go vs development build when relevant.
- React Native New Architecture if enabled.
- light/dark and theme transition.
- Reduce Motion/high contrast/reduced transparency where available.
- list scrolling and navigation transitions.
- orientation/safe-area/keyboard.
- unmount/remount and memory/GPU resource cleanup.
