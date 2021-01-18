#! /bin/zsh

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
clipit &
nm-applet &
feh --bg-fill --randomize $HOME/Pictures/Wallpeper/Dark/*
$HOME/.config/script/picom-blur &
export QT_QPA_PLATFORMTHEME="qt5ct" &

