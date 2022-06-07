from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
from libqtile import qtile
from textwrap import fill
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from colors import gruvbox


mod = "mod4"
myTerm = "kitty"
myBrowser = "brave"
home = os.path.expanduser('~')

#######################################
##          KEY BINDINGS             ##
#######################################

keys = [
    # EXIT keys
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "x", lazy.spawn("archlinux-logout")),
    Key([mod, "control"], "p", lazy.spawn("shutdown now")),
    Key([mod, "control"], "k", lazy.spawn(
        "betterlockscreen -l dim -- --time-str='%H:%M'")),

    # Run app
    Key([mod], "p", lazy.spawncmd()),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "f", lazy.spawn("thunar")),
    Key([mod], "b", lazy.spawn(myBrowser)),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([mod], "s", lazy.spawn("rofi -show")),
    Key([mod], "F11", lazy.spawn("rofi-theme-selector")),
    Key([mod], "F12", lazy.spawn("xfce4-terminal --drop-down")),

    # QTILE LAYOUT KEYS
    # Layout
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "m", lazy.window.toggle_maximize()),
    Key([mod], "n", lazy.window.toggle_minimize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod, "shift"], "l", lazy.layout.flip()),

    # CHANGE WINDOW FOCUS
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),

    # CHANGE MONITOR FOCUS
    Key([mod], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),

    # RESIZE
    Key([mod, "control"], "l",
        lazy.layout.grow()
        ),
    Key([mod, "control"], "h",
        lazy.layout.shrink(),
        ),
    # Key([mod, "control"], "k",
    #     lazy.layout.grow_up(),
    #     lazy.layout.grow(),
    #     lazy.layout.decrease_nmaster(),
    #     ),
    # Key([mod, "control"], "j",
    #     lazy.layout.grow_down(),
    #     lazy.layout.shrink(),
    #     lazy.layout.increase_nmaster(),
    #     ),



    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # ADUO KEYS
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


##############################################
##            Workspace Icons               ##
##############################################

# groups = [
#     Group('1', label="一", layout="monadtall"),
#     Group('2', label="二", layout="monadtall"),
#     Group('3', label="三", layout="monadtall"),
#     Group('4', label="四", layout="monadtall"),
#     Group('5', label="五", layout="monadtall"),
#     Group('6', label="六", layout="monadtall"),
#     Group('7', label="七", layout="monadtall"),
#     Group('8', label="八", layout="monadtall"),
#     Group('9', label="九", layout="monadtall"),
# ]

# groups = [
#     Group("WWW", layout='monadtall'),
#     Group("SYSTEM", layout='monadtall'),
#     Group("CODE", layout='monadtall'),
#     Group("DOC", layout='monadtall'),
#     Group("MUS", layout='monadtall'),
#     Group("vBOX", layout='monadtall'),
# ]
 #  ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   ",
groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label=""),
    Group("6", label=""),
    Group("7", label=""),
]

dgroups_key_binder = simple_key_binder("mod4")


def init_layout_theme():
    return {"margin": 8,
            "border_width": 0,
            "border_focus": "#71a381",
            "border_normal": "#4c566a",
            "single_border_width": 0,
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    #layout.Floating(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #  layout.Max(**layout_theme),
    #  layout.Bsp(**layout_theme),
    #  layout.Stack(stacks=2, **layout_theme),
    #  layout.Columns(**layout_theme),
    #  layout.Tile(shift_windows=True, **layout_theme),
    #  layout.VerticalTile(**layout_theme),
    #  layout.Matrix(**layout_theme),
    #  layout.Zoomy(**layout_theme)
]

# COLORS FOR THE BAR


def init_colors():
    return[
    ["#021b21", "#021b21"],  # 0
    ["#032c36", "#065f73"],  # 1
    # ["#032c36", "#61778d"],# 1 this one is bit lighter, it is for inactive workspace icons.
    ["#e8dfd6", "#e8dfd6"],  # 2
    ["#c2454e", "#c2454e"],  # 3
    ["#44b5b1", "#44b5b1"],  # 4
    ["#9ed9d8", "#9ed9d8"],  # 5
    ["#f6f6c9", "#f6f6c9"],  # 6
    ["#61778d", "#61778d"],  # 7
    ["#e2c5dc", "#e2c5dc"],  # 8
    ["#5e8d87", "#5e8d87"],  # 9
    ["#032c36", "#032c36"],  # 10
    ["#2e3340", "#2e3340"],  # 11
    ["#065f73", "#065f73"],  # 12
    ["#8a7a63", "#8a7a63"],  # 13
    ["#A4947D", "#A4947D"],  # 14
    ["#BDAD96", "#BDAD96"],  # 15
    ["#a2d9b1", "#a2d9b1"],  # 16
]


colors = init_colors()


#########################
##      BAR WIDGETS    ##
#########################

def init_widgets_defaults():
    return dict(font="Hurmit Nerd Font",
                fontsize=12,
                padding=2,
                background=colors[2])


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
        widget.TextBox(
            # text="  ",
            text="  ",
            fontsize="18",
            background=colors[6],
            foreground=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun -modi drun")
            },
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[6],
            foreground=colors[0],
        ),
        widget.GroupBox(
            font="Hack Nerd Font",
            fontsize=16,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=gruvbox['bg'],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Prompt(
            prompt="{0}@{1}: ".format(os.environ["USER"],
                                      socket.gethostname()),
            background=colors[0],
            bell_style='audible',
            foreground=gruvbox['red'],
            cursor=True,
            cursor_blink=0.5,
            max_history=100,
            fontsize=12
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize=33,
            padding=0,
            background=colors[0],
            foreground=gruvbox['bg'],
        ),
        widget.WindowName(
            background=gruvbox['bg'],
            foreground=colors[7],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=gruvbox['bg'],
            foreground=colors[10],
        ),
        widget.WindowCount(
            foreground=colors[2],
            background=colors[10],
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.45,
            padding=0,
            background=colors[10],
            foreground=colors[2],
            fontsize=14,
        ),
        widget.CurrentLayout(
            background=colors[10],
            foreground=colors[2],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[10],
            foreground=colors[11],
        ),
        widget.TextBox(
            text=" ",
            fontsize=14,
            padding=0,
            background=colors[11],
            foreground=colors[2],
        ),
        widget.DF(
            fmt="{}",
            partition="/home",
            format="{uf}{m} ({r:.0f}%)",
            visible_on_warn=False,
            background=colors[11],
            foreground=colors[2],
            padding=5,
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[11],
            foreground=colors[12],
        ),
        widget.TextBox(
            text=" ",
            fontsize=18,
            foreground=colors[2],
            background=colors[12],
            padding=0,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Memory(
            background=colors[12],
            foreground=colors[2],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('kitty -e bashtop')},
            fmt='{}',
            measure_mem = 'G',
        ),
        widget.Sep(
            padding=8,
            linewidth=0,
            background=colors[12],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[12],
            foreground=colors[7],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[7],
        ),
        widget.TextBox(
            text="龍 ",
            fontsize=18,
            padding=0,
            background=colors[7],
            foreground=colors[2],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.CPU(
            format='{freq_current}GHz {load_percent}%',
            background=colors[7],
            foreground=colors[2],
            icons_size=18,
            padding=4,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[7],
            foreground=colors[13],
        ),
        widget.TextBox(
            text="墳 ",
            fontsize=18,
            background=colors[13],
            foreground=colors[0],
        ),
        widget.Volume(
            background=colors[13],
            foreground=colors[0],
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("kitty -e pulsemixer")},
        ),
        # Doesn't work with Spotify so its disabled!
        # widget.TextBox(
        #    text="\u2572",
        #    font="Inconsolata for powerline",
        #    fontsize="33",
        #    padding=0,
        #    background=colors[13],
        #    foreground=colors[0],
        # ),
        # widget.Mpd2(
        #   background=colors[13],
        #   foreground=colors[0],
        #   idle_message=" ",
        #   idle_format="{idle_message} Not Playing",
        #   status_format="  {artist}/{title} [{updating_db}]",
        #   font="Iosevka Nerd Font",
        #   fontsize=15,
        # ),
        # This one works with Spotify, enable if you want!
        # widget.Mpris2(
        #    background=colors[13],
        #    foreground=colors[0],
        #    name="spotify",
        #    objname="org.mpris.MediaPlayer2.spotify",
        #    fmt="\u2572   {}",
        #    display_metadata=["xesam:title", "xesam:artist"],
        #    scroll_chars=20,
        #    font="Iosevka Nerd Font",
        #    fontsize=15,
        # ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[13],
            foreground=colors[14],
        ),
        widget.KeyboardLayout(
            fmt=" {} הּ ",
            configured_keyboards=["gb", "us"],
            padding=0,
            background=colors[14],
            foreground=colors[0],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[14],
            foreground=colors[15],
        ),
        widget.TextBox(
            text="  ",
            fontsize="14",
            padding=0,
            background=colors[15],
            foreground=colors[0],
        ),
        widget.Clock(
            foreground=colors[0],
            background=colors[15],
            format="%A, %B %d",
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[15],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[15],
            foreground=colors[16],
        ),
        widget.TextBox(
            text=" ",
            fontsize="18",
            padding=0,
            background=colors[16],
            foreground=colors[0],
            #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty feh --recursive --bg-scale --randomize ~/images/wallpapers/")},
        ),
        widget.Clock(
            foreground=colors[0],
            background=colors[16],
            format="%H:%M",
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[16],
            foreground=colors[6],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=25, opacity=1, margin=[8,8,0,8])),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=25, opacity=1, margin=[8,8,0,8]))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


#dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


# @hook.subscribe.startup
# def start_always():
#     # Set the cursor to something sane in X
#     subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


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


auto_fullscreen = True
focus_on_window_activation = 'focus'  # smart
reconfigure_screens = True


# STARTUP
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


wmname = "LG3D"
