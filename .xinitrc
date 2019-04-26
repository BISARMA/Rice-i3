if [[ -f ~/.Xresources ]]; then
  xrdb -load ~/.Xresources
fi

xset +fp ~/.local/share/fonts

exec i3
