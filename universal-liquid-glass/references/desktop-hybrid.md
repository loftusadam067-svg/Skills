# Desktop and hybrid frontends

Use for Electron, Tauri, pywebview, Qt/QML, .NET MAUI/WPF/WinUI/Avalonia and custom desktop shells.

## First question: what is the backdrop?

A desktop webview normally cannot sample arbitrary pixels from other applications behind its window using ordinary CSS. Before promising true desktop refraction, determine whether the material is meant to refract:

1. content inside the application window;
2. a controlled wallpaper/image/scene;
3. the real desktop/other windows behind a transparent native window.

These require different architectures.

## In-app content

If glass only refracts the application's own content, use the normal web/native rendering path. Electron/Tauri web content follows `web.md`; native Qt/.NET views should use compositor/shader effects where supported.

## Real desktop backdrop

To refract the actual desktop behind a transparent window, the renderer needs a source texture. Typical architecture:

```text
host/native process
  -> obtains wallpaper or permissioned live screen/window capture
  -> provides frame + window coordinates/scale
renderer
  -> aligns backdrop texture with window
  -> applies glass refraction/diffusion
  -> overlays crisp semantic UI
```

Do not claim a CSS-only implementation can see through a webview to arbitrary other windows.

Security/privacy:
- live screen capture may require OS permission;
- disclose capture clearly;
- do not persist captured frames unless product requirements explicitly require it;
- pause capture when hidden/minimized;
- handle permission denial with a safe wallpaper/frost/opaque fallback.

## Electron

- Prefer Chromium rendering for in-app content glass.
- For true desktop capture, use Electron/native capture APIs only with explicit product justification and privacy handling.
- Send frame/position data over efficient IPC; avoid base64-encoding full-resolution frames each animation tick.
- Keep one shared renderer/source where multiple lenses are visible.
- Account for display scale changes when moving between monitors.
- Pause GPU/RAF/capture work when the window is occluded, minimized or static.

## Tauri

- Use web rendering for in-app optics.
- For real desktop capture/transparency, implement a minimal Rust/native command/plugin rather than a high-frequency JS bridge that serializes large images.
- Keep permissions scoped and platform-specific.
- Verify WebView engine differences: macOS uses WebKit while Windows commonly uses WebView2, so an SVG/backdrop path that works on Chromium may not work on macOS.

## pywebview

For real desktop glass, Python can provide wallpaper/live capture and window coordinates while the webview renders a WebGL scene. Avoid pushing huge PNG/base64 strings every frame; use the most efficient binary/texture path available to the host stack. Gracefully degrade when screen recording permission is denied.

## Qt/QML

- Prefer QML/Qt Quick scene graph effects or custom shaders for controlled scene refraction.
- Keep hit testing/accessibility on ordinary controls.
- Share shader/material instances where possible.
- Verify graphics backend behavior (Metal/Direct3D/Vulkan/OpenGL depending target).
- For OS backdrop/acrylic/mica-like native surfaces, use platform-native window effects when they fit the design; do not call them Apple's native Liquid Glass.

## .NET

### WinUI / Windows App SDK

Use Windows-native composition/backdrop materials where product-appropriate, then add restrained shape/rim hierarchy if an Apple-inspired glass treatment is desired. Windows Mica/Acrylic are distinct materials; label them accurately.

### WPF

WPF does not provide Apple's material. Prefer Windows composition/interoperability or a bounded shader/effect only when the cost is justified. Avoid per-frame software bitmap effects.

### .NET MAUI

Share semantic tokens and component behavior while using platform handlers/native views for high-fidelity platform-specific effects. Apple targets can bridge to public Apple APIs; Android uses an emulation/fallback.

### Avalonia

Use compositor/custom shader capabilities supported by the current Avalonia renderer and platform backdrop options. Verify actual backend support before choosing an effect.

## Window behavior

Desktop glass must survive:
- resize;
- maximize/fullscreen;
- moving between displays with different scale/color profiles;
- inactive window state;
- window shadows/rounded corners;
- virtual desktops/spaces;
- remote desktop where GPU effects may differ;
- screen capture permissions;
- battery saver and integrated GPUs.

Never tie optical coordinates to stale window positions.

## Performance

- Wallpaper mode can be nearly static and cheap.
- Live desktop capture should use a deliberately bounded frame rate unless full-rate motion is necessary.
- Keep capture resolution no higher than the optical layer needs.
- Reuse GPU textures and allocations.
- Park rendering/capture when unchanged.
- Avoid multiple independent capture pipelines for multiple lenses.

## Accessibility

Transparent desktop windows can create unpredictable contrast. Provide a high-legibility mode with stronger diffusion or an opaque fallback. Preserve native focus/keyboard shortcuts and platform accessibility APIs.

## Verification

Test multiple monitors/DPI, window movement, resize, fullscreen, inactive state, permission denial, dark/light desktop backgrounds, dynamic wallpaper, integrated GPU, remote desktop where relevant, and graceful fallback when transparency/capture is unavailable.
