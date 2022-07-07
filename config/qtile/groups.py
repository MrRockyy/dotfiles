from libqtile.config import Group, Key
from libqtile.lazy import lazy
from keys import keys , mod
import libqtile 

groups = [Group(i) for i in [
    "   ", "  ", "   ","   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    @libqtile.hook.subscribe.client_new
    def func(c):
      if c.name == "firefox":
        c.togroup("a")
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

