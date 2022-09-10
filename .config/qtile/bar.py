import os
import socket
from libqtile import qtile, widget
from colors import gruvbox

# Colors for the bar
colors = [
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

gr_colors = {
    'dark-gray': '#3A3845'
}


# Bar widgets
widget_defaults = dict(
    font="Hurmit Nerd Font",
    fontsize=10,
    padding=2,
)


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
        widget.TextBox(
            text="  ",
            fontsize="12",
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
            foreground=colors[11],
        ),
        widget.TextBox(
            text=" ",
            fontsize=12,
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
            fontsize="33",
            padding=0,
            background=colors[11],
            foreground=colors[12],
        ),
        widget.TextBox(
            text=" ",
            fontsize=16,
            foreground=colors[2],
            background=colors[12],
            padding=0,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Memory(
            background=colors[12],
            foreground=colors[2],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('kitty -e bashtop')},
            fmt='{}',
            measure_mem='G',
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
            fontsize=16,
            padding=0,
            background=colors[7],
            foreground=colors[2],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.CPU(
            format='{freq_current}GHz {load_percent}%',
            background=colors[7],
            foreground=colors[2],
            icons_size=18,
            padding=4,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[7],
            foreground=gruvbox['bg'],
        ),

        widget.WindowName(
            fontsize=10,
            background=gruvbox['bg'],
            foreground=colors[7],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=gruvbox['bg'],
            foreground='#3A3845',
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background='#3A3845',
            foreground='#3A3845',
        ),
        widget.GroupBox(
            font="Hack Nerd Font",
            fontsize=12,
            padding_y=9,
            padding_x=9,
            borderwidth=2,
            active='#EEEEEE',
            inactive=gruvbox['gray'],
            rounded=False,
            highlight_color=gruvbox['bg'],
            highlight_method="line",
            this_current_screen_border='#FF4C29',
            this_screen_border='#EEB76B',
            other_current_screen_border='#FF4C29',
            other_screen_border='#EEB76B',
            foreground=colors[2],
            background='#3A3845'
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background='#3A3845',
            foreground='#3A3845',
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background='#3A3845',
            foreground=gruvbox['bg'],
        ),

        widget.Spacer(length=350, background=gruvbox['bg']),


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
            fontsize=11,
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
            foreground=colors[13],
        ),
        widget.TextBox(
            text="墳 ",
            fontsize=14,
            background=colors[13],
            foreground=colors[0],
        ),
        widget.Volume(
            background=colors[13],
            foreground=colors[0],
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn(
                "kitty -e pulsemixer")},
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
            configured_keyboards=["us", "es", 'gb'],
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
            fontsize="12",
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
            fontsize="14",
            padding=0,
            background=colors[16],
            foreground=colors[0],
            #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty feh --recursive --bg-scale --randomize ~/images/wallpapers/")},
        ),
        widget.Clock(
            foreground=colors[0],
            background=colors[16],
            format="%H:%M",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[16],
            foreground=colors[6],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
    ]
    return widgets_list
