```
   #### In JaKooLit:

        * Typically used for desktop overview (`ags -t 'overview'`), and sometimes for
     custom "alt tab", dashboard, etc.
        * Can be used as *bar* itself or for "overlays" (e.g. GNOME Activities,
    Exposé).

    ----------------------------------------------------------------------------------
    ---

    # 2. What's New in AGS v2 vs v1?

    ┌───────────────┬──────────────────────────────────────────────┬──────────────────
    ───────────────────────────────────────────────────────┐
    │               │ AGS v1 (Legacy: you have now)                │ AGS v2 (Current, 
    active)                                                │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Config        │ Javascript, more ad-hoc API                  │ TypeScript, with
    typed API                                              │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Extensibility │ More limited scripting, quirks               │ Much more
    flexible/event-based                                          │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Docs          │ Legacy (unstable)                            │ Active
    (https://aylur.github.io/ags)                                    │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Community     │ Declining, almost no new widgets             │ Growing set of v2
     setups, themes                                        │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Features      │ Overview, bar, popups (limited)              │ Bar, overview,
    dashboards, popups, much richer widgets, better gestures │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Performance   │ Fine for small dashboards                    │ More scalable,
    cleaner IPC                                              │
    ├───────────────┼──────────────────────────────────────────────┼──────────────────
    ───────────────────────────────────────────────────────┤
    │ Package       │ v1 EOL, v2: active Nixpkgs and flake support │ v2 well supported
     everywhere                                            │
    └───────────────┴──────────────────────────────────────────────┴──────────────────
    ───────────────────────────────────────────────────────┘

        * **v2** is a massive upgrade—cleaner config, more widgets, better Wayland
    integration.
        * All new community work is on v2.

    ----------------------------------------------------------------------------------
    ---

    # 3. Are There Good Online AGS v2 Example Configs?

    Yes!
    Here are some ready-to-clone AGS v2 configs and showcases:

        * **Official AGS v2 Examples:**
            * https://github.com/Aylur/ags/tree/main/examples/
        * **Popular AGS v2 Dotfiles:**
            * https://github.com/Aylur/ags/wiki/Community-Themes-and-Examples

            * https://github.com/unRob/ags-config (minimal but clear)

            * https://github.com/ImLore/ags-config (some cool overlays)

            * https://github.com/alexays/Waybar/issues/1069#issuecomment-1705346842
    (people posting AGS bars for Hyprland)

            * Search GitHub for `"ags" hyprland` — tons of configs.

    YouTube Demos:

        * ["AGS v2 configuration"
    playlist](https://www.youtube.com/results?search_query=ags+hyprland+v2)
        * ["hyprland ags
    bar"](https://www.youtube.com/results?search_query=hyprland+ags+bar)

    ----------------------------------------------------------------------------------
    ---

    # 4. Migrating: v1 → v2, and Getting Started

        * Remove the v1 flake, add v2 as input (`url = "github:Aylur/ags"` for v2).
        * Grab an example config:
            * `git clone https://github.com/Aylur/ags`

            * Copy an `examples/` config to `~/.config/ags` (for v2).
        * The `overview`, `alt-tab`, and much more is possible in AGS v2 out of the
    box—or via community modules.
        * Switch keybinds to the new AGS v2 CLI if needed.

    Note: AGS v2 config is in TypeScript—copy/paste from examples is easiest, editing 
    requires only minor TypeScript basics (you can follow existing patterns without 
    knowing the language deeply).

    ----------------------------------------------------------------------------------
    ---

    # TL;DR steps for you:

        1. **Try a AGS v2 example config** (clone & copy to `~/.config/ags`)
        2. **Switch your flake input to v2** and rebuild.
        3. **Update any `ags -t` calls in keybinds/scripts** (if the v2 CLI changed).
        4. **Test** — if “alt-tab”/overview is visible, customize more.

    ----------------------------------------------------------------------------------
    ---

    Would you like…

        * A **step-by-step guide to migrate to AGS v2** on your NixOS setup?
        * **A curated ready-to-use AGS v2 config** you can drop in?
        * Or just more details on how to dig into all the AGS v2 features?

    Let me know how hands-on you want the help!
```