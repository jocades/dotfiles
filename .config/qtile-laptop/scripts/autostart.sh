#!/bin/bash

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# Wallpaper
#run feh --bg-scale --no-xinerama /home/j0rdi/images/morning.png &
run feh --bg-fill /home/j0rdi/images/wallpapers/nord/the-great-wave.png &
# ~/.fehbg &

# Display
run xrandr --output eDP1 --mode 1920x1080
#autorandr horizontal

#Set native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

# Mount CloudDrives
rclone --vfs-cache-mode writes mount onedrive: ~/cloud/onedrive &
run rclone --vfs-cache-mode writes mount gdrive: ~/cloud/gdrive &

# Sxhkd Daemon KeyBinds
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

# Utlities & Services
cbatticon -u 5 &
run variety &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
