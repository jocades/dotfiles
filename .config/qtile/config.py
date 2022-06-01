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

groups = [
    Group("WWW", layout='monadtall'),
    Group("SYSTEM", layout='monadtall'),
    Group("CODE", layout='monadtall'),
    Group("DOC", layout='monadtall'),
    Group("MUS", layout='monadtall'),
    Group("vBOX", layout='monadtall'),
]

dgroups_key_binder = simple_key_binder("mod4")


def init_layout_theme():
    return {"margin": 5,
            "border_width": 2,
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
    return[["#282c34", "#282c34"],  # 0
           ["#1c1f24", "#1c1f24"],  # 1
           ["#dfdfdf", "#dfdfdf"],  # 2
           ["#ff6c6b", "#ff6c6b"],  # 3
           ["#98be65", "#98be65"],  # 4
           ["#da8548", "#da8548"],  # 5
           ["#51afef", "#51afef"],  # 6
           ["#c678dd", "#c678dd"],  # 7
           ["#46d9ff", "#46d9ff"],  # 8
           ["#a9a1e1", "#a9a1e1"],  # 9
           ["#a3be8c", "#a3be8c"],  # 10
           ["#bf616a", "#bf616a"],  # 11
           ["#88c0d0", "#88c0d0"]]  # 12


colors = init_colors()


#########################
##      BAR WIDGETS    ##
#########################

def init_widgets_defaults():
    return dict(font="Hack",
                fontsize=10,
                padding=2,
                background=colors[2])


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Image(
            filename="~/.config/qtile/icons/python.png",
            scale="False",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(f'rofi -show drun')}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=gruvbox['green'],
            rounded=False,
            highlight_color=colors[1],
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
            max_history=100
        ),
        widget.TextBox(
            text='|',
            font="FontAwesome",
            background=colors[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.WindowCount(
            foreground=colors[2],
            background=colors[0],
            
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="FontAwesome",
            background=colors[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            font="FontAwesome",
            background=colors[0],
            foreground=colors[12],
            padding=0,
            fontsize=37
        ),
        widget.Net(
            font="Hack Nerd Font",
            foreground=colors[1],
            background=colors[12],
            format = '直 {down} ↓↑{up}',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="FontAwesome",
            background=colors[12],
            foreground=colors[10],
            padding=0,
            fontsize=37
        ),
        widget.Memory(
            font="Hack Nerd Font",
            foreground=colors[1],
            background=colors[10],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('kitty htop')},
            fmt=' {}',
            measure_mem = 'G',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="FontAwesome",
            background=colors[10],
            foreground=colors[11],
            padding=0,
            fontsize=37
        ),
        widget.CPU(
            font='Hack Nerd Font',
            format=' {freq_current}GHz {load_percent}%',
            foreground=colors[1],
            background=colors[11],
        ),
        widget.TextBox(
            text='',
            font="FontAwesome",
            background=colors[11],
            foreground=colors[10],
            padding=0,
            fontsize=37
        ),
        widget.Volume(
            font="Hack Nerd Font",
            foreground=colors[1],
            background=colors[10],
            fmt='奔 {}',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="FontAwesome",
            background=colors[10],
            foreground=colors[11],
            padding=0,
            fontsize=37
        ),
        widget.NvidiaSensors(
            font="Hack Nerd Font",
            foreground=colors[1],
            background=colors[11],
            threshold=90,
            fmt=' {}',
            padding=5
        ),
        widget.TextBox(
            text='',
            font="FontAwesome",
            background=colors[11],
            foreground=colors[10],
            padding=0,
            fontsize=37
        ),
        widget.Clock(
            font="Hack Nerd Font",
            foreground=colors[1],
            background=colors[10],
            format=" %A, %B %d - %H:%M"
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
    return [Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=1)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1))]


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
