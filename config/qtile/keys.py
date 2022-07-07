from libqtile.config import Key
from libqtile.lazy import lazy
# keys
user="sarch"
mod = "mod4"
terminal = "terminator"
fileExplorer="pcmanfm"
appMenu="rofi -show drun"
musicPlayer="spotify"
browser="firefox"
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    #-------------------APPS --------------------------------------
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod],"b",lazy.spawn(browser),desc="launch navegator"),
    Key([mod], "m",lazy.spawn("/home/sarch/.config/qtile/launcher.sh"), desc="launch app menu"),
    Key([mod], "p",lazy.spawn(musicPlayer), desc="launch music player"),
    Key([mod], "e",lazy.spawn(fileExplorer), desc="launch file explorer "),
    Key([mod], "q",lazy.spawn("/home/sarch/.config/qtile/powermenu.sh"), desc="launch file explorer "),
    #-----------------------SYSTEM SHORCUTS---------------------------------------
#volume 

    Key([mod], "F11", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -3%")),
    Key([mod], "F12", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +3%")),
    Key([mod], "F10", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

#brigtness
    Key([mod], "F6", lazy.spawn("brightnessctl set +3%")),
    Key([mod], "F5", lazy.spawn("brightnessctl set 3%-")),

#eye protection 
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

#screenshot 
    Key([mod], "s", lazy.spawn(f"scrot /home/{user}/Pictures/screenshots/screen.png")),
    Key([mod, "shift"], "s", lazy.spawn(f"scrot -s /home/{user}/Pictures/screenshots/screen.png ")),
    #--------------------------------------------------------------------------
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

