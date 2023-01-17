import os
import subprocess
from libqtile import layout, bar, hook
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen, Rule
from libqtile.command import lazy
from bar import widget_defaults, init_widgets_list
# from thin_bar import widget_defaults, init_widgets_list


mod = "mod4"
terminal = "kitty"
browser = "brave"
editor = "code"
file_manager = "thunar"

keys = [
    # Qtile window manager
    Key([mod, "control"], "r", lazy.restart(), desc='Restart Qtile'),
    Key([mod, "control"], "p", lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod, "control"], "s", lazy.spawn(
        f'{terminal} --hold -e python3 .config/qtile/scripts/qtile-keys'), desc='Show qtile keys'),


    # Common
    Key([mod], "q", lazy.window.kill(), desc='Kill window'),
    Key([mod], "x", lazy.spawn("archlinux-logout"), desc='Logout menu'),
    Key([mod, "control"], "y", lazy.spawn(
        "betterlockscreen -l dim -- --time-str='%H:%M'"), desc='Lock screen'),
    Key([mod], "p", lazy.spawncmd(), desc='Spawn prompt in the bar'),

    # Launch
    Key([mod], "Return", lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod, 'shift'], "Return", lazy.spawn(
        f'{terminal} -e tmux a'), desc='Launch tmux terminal attached to last session'),
    Key([mod, 'shift'], "f", lazy.spawn(
        file_manager), desc='Launch file manager'),
    Key([mod], "b", lazy.spawn(browser), desc='Launch browser'),
    Key([mod], "c", lazy.spawn("code"), desc='Launch vscode'),
    Key([mod], 'd', lazy.spawn("discord")),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc='Spawn app launcher'),
    Key([mod], "F11", lazy.spawn("rofi-theme-selector"), desc='Change rofi theme'),

    # Toggle between layouts
    Key([mod], "space", lazy.next_layout(), desc='Toggle between layouts'),

    # Monitor focus
    Key([mod], "w", lazy.to_screen(0), desc='Focus monitor 1'),
    Key([mod], "e", lazy.to_screen(1), desc='Focus monitor 2'),
    Key([mod], "t", lazy.to_screen(2), desc='Focus monitor 3'),

    # Window focus
    Key([mod], "h", lazy.layout.left(), desc='Focus window left'),
    Key([mod], "l", lazy.layout.right(), desc='Focus window right'),
    Key([mod], "j", lazy.layout.down(), desc='Focus window down'),
    Key([mod], "k", lazy.layout.up(), desc='Focus window up'),
    Key([mod], "s", lazy.spawn("rofi -show"), desc='Show open windows'),

    # Window move
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Window resize
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc='Toggle window fullscreen'),
    Key([mod], "m", lazy.window.toggle_maximize(),
        desc='Toggle window maximize'),
    Key([mod], "n", lazy.window.toggle_minimize(),
        desc='Toggle window minimize'),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc='Toggle window floating'),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),


    # Media
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)


# Move window to screen
keys.extend([
    Key([mod, "shift"], "Right", lazy.function(window_to_next_screen,
        switch_screen=True), desc='Move window to right screen'),
    Key([mod, "shift"], "Left", lazy.function(window_to_previous_screen,
        switch_screen=True), desc='Move window to left screen'),
])


#  ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   ", 

groups = [
    Group("1", label="1", layout='columns', spawn=browser),
    Group("2", label="2", layout='columns'),
    Group("3", label="3", layout='columns'),
    Group("4", label="6"),
    Group("5", label="9"),
    Group("6", label=""),
    Group("7", label="ﭮ"),
    Group("8", label=""),
    Group("9", label=""),
]

for i in groups:
    keys.extend([
        # Switch workspace
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc=f'Switch to workspace {i.name}'),
        Key([mod], "Tab", lazy.screen.next_group(),
            desc='Switch to next workspace'),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group(),
            desc='Switch to previous workspace'),

        # Move window to workspace and follow
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen(),
            desc='Move window to workspace and follow'),

        # Move window to workspace and stay
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])


groups.append(ScratchPad('scratchpad', [
    DropDown('term', terminal, width=0.8, height=0.8, x=0.1, y=0.1),
    DropDown('files', file_manager, width=0.35, height=0.8, x=0.3, y=0.1),
    DropDown('search', 'firefox', width=0.6, height=0.8, x=0.2, y=0.1),
]))

keys.extend([
    Key(['mod1'], '1', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(['mod1'], '2', lazy.group['scratchpad'].dropdown_toggle('files')),
    Key(['mod1'], '3', lazy.group['scratchpad'].dropdown_toggle('search')),
])


main_theme = {
    "margin": 5,
    "single_border_width": 0,
    "border_width": 1,
    "border_focus": "#71a381",
    "border_normal": "#4c566a",
}

columns_theme = {
    'margin': 0,
    'margin_on_single': 0,
    'border_on_single': False,
    "border_width": 1,
    "border_focus": "#71a381",
    "border_normal": "#4c566a",
}

layouts = [
    layout.Columns(**columns_theme),
    layout.MonadTall(**main_theme),
    layout.MonadWide(**main_theme),
    layout.Floating(**main_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Max(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme)
]


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


# Mouse config
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=18, opacity=1, margin=[0, 0, 0, 0])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=18, opacity=1, margin=[0, 0, 0, 0]))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'focus'
reconfigure_screens = True


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='arcolinux-logout'),
    Match(wm_class='xfce4-terminal'),
])


# Startup
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


wmname = "LG3D"
