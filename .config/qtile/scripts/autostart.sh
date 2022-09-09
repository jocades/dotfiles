#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# Remap CONTROL with CAPS_LOCK 
# EXAMPLE:
# clear lock
# clear control
# keycode 66 = Control_L Caps_Lock NoSymbol NoSymbol
# keycode 37 = Caps_Lock
# add control = Caps_Lock Control_L Control_R

# Wallpaper
#run feh --bg-scale --no-xinerama /home/j0rdi/images/morning.png &
run feh --bg-fill /home/j0rdi/images/wallpapers/nord/the-great-wave.png &
# ~/.fehbg &

# Display
run xrandr --output DVI-D-0 --primary --mode 1920x1080 --pos 0x0 --rate 143.92 --output HDMI-0 --mode 1920x1080 --pos 1920x0
#run xrandr --output HDMI-0 --primary --mode 1920x1080 --rate 143.92 --output DVI-D-0 --mode 1920x1080
#run xrandr --output HDMI-0 --primary --mode 1920x1080 --rate 143.92
#autorandr horizontal

#Set native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

# Mount OneDrive
sh -c "rclone --vfs-cache-mode writes mount onedrive: ~/onedrive" &

# Start sxhkd to replace Qtile native key-bindings
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

# Start utility applications at boot time
run variety &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
