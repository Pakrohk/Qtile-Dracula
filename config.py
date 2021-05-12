#! /bin/python
# -*- coding: utf-8 -*-
#################################################################################
##Qtile Config PowerBy:#########################################################
############    _    _     _         _    _              _     _    #############
############   / \  | |   (_)_ __   / \  | | ___ __ ___ | |__ | | __#############
############  / _ \ | |   | | '_ \ / _ \ | |/ / '__/ _ \| '_ \| |/ /#############
############ / ___ \| |___| | |_) / ___ \|   <| | | (_) | | | |   < #############
############/_/   \_\_____|_| .__/_/   \_\_|\_\_|  \___/|_| |_|_|\_\#############
############                |_|                                     #############
####################################################################28,sep,2020##
#################################################################################

import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

# WM Name
wmname = "qtile"
# my short name keys
SUPER = "mod4"
ALT = "mod1"
CTRL = "control"
PRT_SC = "Print"
fnUP = "XF86AudioRaiseVolume"
fnDOWN = "XF86AudioLowerVolume"
fnVoff = "XF86AudioMute"
RET = "Return"
SPC = "space"
# My short name apps
TERM = "kitty"
EDITOR = "nvim"
BRS = "chromium"
FileManager = "pcmanfm-qt"

keys = [
    # QTILE LAYOUT KEYS
    Key([SUPER], "n", lazy.layout.normalize()),
    # Switch window focus to other pane(s) of stack
    Key([SUPER], "space", lazy.layout.next()),
    # CHANGE FOCUS
    Key([SUPER], "Up", lazy.layout.up()),
    Key([SUPER], "Down", lazy.layout.down()),
    Key([SUPER], "Left", lazy.layout.left()),
    Key([SUPER], "Right", lazy.layout.right()),
    Key([SUPER], "k", lazy.layout.up()),
    Key([SUPER], "j", lazy.layout.down()),
    Key([SUPER], "h", lazy.layout.left()),
    Key([SUPER], "l", lazy.layout.right()),

    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([SUPER, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([SUPER, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([SUPER, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([SUPER, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([SUPER, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([SUPER, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([SUPER, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([SUPER, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([SUPER, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([SUPER, ALT], "k", lazy.layout.flip_up()),
    Key([SUPER, ALT], "j", lazy.layout.flip_down()),
    Key([SUPER, ALT], "l", lazy.layout.flip_right()),
    Key([SUPER, ALT], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([SUPER, "shift"], "k", lazy.layout.shuffle_up()),
    Key([SUPER, "shift"], "j", lazy.layout.shuffle_down()),
    Key([SUPER, "shift"], "h", lazy.layout.shuffle_left()),
    Key([SUPER, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([SUPER, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([SUPER, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([SUPER, "shift"], "Left", lazy.layout.swap_left()),
    Key([SUPER, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([SUPER, "shift"], "space", lazy.window.toggle_floating()),
    # Swap panes of split stack
    Key([SUPER, "shift"], SPC, lazy.layout.rotate()),
    # multiple stack panes
    Key([SUPER, "shift"], RET, lazy.layout.toggle_split()),
    # Screen Shot with flameshot
    Key([], PRT_SC, lazy.spawn("flameshot full -p /home/ap/Pictures/Screenshots ")),
    Key(
        [SUPER],
        PRT_SC,
        lazy.spawn("flameshot gui -p /home/ap/Pictures/Screenshots/"),
    ),
    # applications shortcat
    Key([SUPER], RET, lazy.spawn(TERM)),
    Key([SUPER], "b", lazy.spawn(BRS)),
    Key([SUPER], "f", lazy.spawn(FileManager)),
    Key([SUPER], "e", lazy.spawn(TERM + " -e " + EDITOR)),
    Key([SUPER, ALT], "r", lazy.spawn(TERM + " -e ranger")),
    Key([SUPER], "t", lazy.spawn("telegram-desktop")),
    # Toggle between different layouts as defined below
    Key([SUPER], "Tab", lazy.next_layout()),
    Key([SUPER], "w", lazy.window.kill()),
    Key([SUPER, CTRL], "r", lazy.restart()),
    Key([SUPER, CTRL], "q", lazy.shutdown()),
    Key([SUPER], "r", lazy.spawncmd()),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], fnUP, lazy.spawn("amixer -q set Master 5%+")),
    Key([], fnDOWN, lazy.spawn("amixer -q set Master 5%-")),
    Key([], fnVoff, lazy.spawn("amixer -q set Master toggle")),
    # MULTIMEDIA KEYS

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),
    # keyBoardLayout
    Key([ALT], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard()),
    Key([ALT], "Shift_R", lazy.widget["keyboardlayout"].next_keyboard()),
    # Rofi Run
    Key([SUPER], "d", lazy.spawn(""" rofi -show drun run -modi drun,run -show-icon -location 1 -width 100 \
                 -lines 2 -line-margin 0 -line-padding 1 \
                 -separator-style none -font "mono 10" -columns 9 -bw 0 \
                 -disable-history \
                 -hide-scrollbar \
                 -color-window "#222222, #222222, #b1b4b3" \
                 -color-normal "#222222, #b1b4b3, #222222, #005577, #b1b4b3" \
                 -color-active "#222222, #b1b4b3, #222222, #007763, #b1b4b3" \
                 -color-urgent "#222222, #b1b4b3, #222222, #77003d, #b1b4b3" \
                 -kb-row-select "Tab" -kb-row-tab "" """)),

    Key([SUPER, CTRL], "a", lazy.spawn(TERM + " -e rofi-appsmenu")),
    ]
# GROUPS


def init_group_name():
    group_names = [
        ("", {"layout": "tile"}),
        ("", {"layout": "tile"}),
        ("", {"layout": "monadtall"}),
        ("", {"layout": "monadwide"}),
        ("", {"layout": "max"}),
        ("", {"layout": "floating"}),
        ("", {"layout": "floating"}),
    ]
    return group_names


groups = [Group(name, **kwargs) for name, kwargs in init_group_name()]

for i, (name, kwargs) in enumerate(init_group_name(), 1):
    keys.append(
        Key([SUPER], str(i), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([SUPER, "shift"], str(i), lazy.window.togroup(name))
    )  # Send current window to another group

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "e1acff",
    "border_normal": "1D2330",
}

##### THE LAYOUTS #####
layouts = [
    layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    # layout.TreeTab(
    #    font="Ubuntu",
    #    fontsize=14,
    #    sections=["FIRST", "SECOND"],
    #    section_fontsize=11,
    #    bg_color="141414",
    #    active_bg="90C435",
    #    active_fg="000000",
    #    inactive_bg="384323",
    #    inactive_fg="a0a0a0",
    #    padding_y=5,
    #    section_top=10,
    #    panel_width=320,
    # ),
    layout.Floating(**layout_theme),
]

##### COLORS #####
colors = [
    ["#282a36", "#282a36"],  # panel background
    ["#44475a", "#44475a"],  # background for current screen tab
    ["#f8f8f2", "#f8f8f2"],  # font color for group names
    ["#44475a", "#44475a"],  # border line color for current tab
    ["#282a36", "#282a36"],  # border line color for other tab and odd widgets
    ["#44475A", "#44475A"],  # color for the even widgets
    ["#6272a4", "#6272a4"],  # window name
]

##### PROMPT #####
# prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="Ubuntu Mono", fontsize=18, padding=2)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####


def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(scale=0.79),
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[2], background=colors[0]),
        widget.GroupBox(highlight_method="block", inactive="999999"),
        # widget.Prompt(
        #    bell_style="audible",
        # ),
        widget.WindowName(),
        widget.TextBox(text=" Vol:", padding=1),
        widget.Volume(padding=5),
        widget.KeyboardLayout(configured_keyboards=["us", "ir"]),
        widget.Systray(),
        widget.Clock(format="%a %d %b %I:%M %p"),
        widget.Sep(linewidth=0, padding=6,
                   foreground=colors[2], background=colors[0]),
    ]
    return widgets_list


# SCREENS ##### (TRIPLE MONITOR SETUP)


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1  # Slicing removes unwanted widgets on Monitors 1,3


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=30,
                background=['#282a36'],
                opacity=0.88
            )
        ),
        Screen(
            bottom=bar.Bar(
                widgets=init_widgets_screen2(),
                size=35,
                background=["#282a36"],
                opacity=0.8
            )
        ),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag(
        [SUPER],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [SUPER],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([SUPER], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = wmname
