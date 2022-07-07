from libqtile import bar, layout, widget
from libqtile.config import Screen
from spotify import Spotify
import os
dat="%I:%M %p"
def date():
   os.system("terminator -e nmtui")
def nmtui():
   os.system("terminator -e nmtui")
widget_defaults = dict(
    font="UbuntuMono Nerd Font Bold",
    fontsize=16,
    padding=5,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active="#2E8A39",
                inactive="#497366",
                rounded=False,
                highlight_method='block',
                urgent_alert_method='block',
                urgent_border="#ff0000",
                this_current_screen_border="#7aff8a",
                other_screen_border="#12362B",
                this_screen_border="#7aff8a",
                other_current_screen_border="#12362B",
                disable_drag=True


                ),
                widget.Sep(),
                Spotify(max_chars=70 ,
                    format="            {icon}  {artist}:{track}"),
                widget.WindowName(format="{state}"),

                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#10231D", background="#000000"),
                widget.CurrentScreen(background="#10231D",
                                     active_text=" ", inactive_text=" ﯥ "),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#1C3F2E", background="#10231D"),
                widget.Wlan(
                    format="  {essid}", disconnected_message="睊 Disconnected", background="#1C3F2E",mouse_callbacks={"Button1":nmtui}),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#285835", background="#1C3F2E"),
                widget.CurrentLayoutIcon(
                    scale=0.6, font="UbuntuMono Nerd Font", padding=-3, background="#285835"),
                widget.CurrentLayout(background="#285835", padding=2),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#3C8640", background="#285835"),

                widget.Clock(background="#3C8640", format=dat, mouse_callbacks={"Button1":date}), ],

            24, ),),




    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(

                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active="#2E8A39",
                inactive="#497366",
                rounded=False,
                highlight_method='block',
                urgent_alert_method='block',
                urgent_border="#ff0000",
                this_current_screen_border="#7aff8a",
                other_screen_border="#12362B",
                this_screen_border="#7aff8a",
                other_current_screen_border="#12362B",
                disable_drag=True
             
            
           
          
         
        
       
      
     
    
 
   
  






                ),
                widget.Sep(),
                widget.WindowName(max_chars=30,for_curren_screen=False, format="{name}"),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#10231D", background="#000000"),
                widget.TextBox(text="墳",background="#10231D"),
                widget.PulseVolume(background="#10231D"),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#1C3F2E", background="#10231D"),
                widget.Wlan(
                    format="  {essid}", disconnected_message="睊 Disconnected", background="#1C3F2E"),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#285835", background="#1C3F2E"),
                widget.CurrentLayoutIcon(
                    scale=0.6, font="UbuntuMono Nerd Font", padding=-3, background="#285835"),
                widget.CurrentLayout(background="#285835", padding=2),
                widget.TextBox(text="", fontsize=35, padding=-3,
                               foreground="#3C8640", background="#285835"),

                widget.Clock(
                    background="#3C8640",

                    format="%I:%M %p"), ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "

        ),
    ),

]
