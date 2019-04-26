#!/usr/bin/env python3

import subprocess

icons = [
    [
        u"\uf579",
        u"\uf57a",
        u"\uf57b",
        u"\uf57c",
        u"\uf57d",
        u"\uf57e",
        u"\uf57f",
        u"\uf580",
        u"\uf581",
        u"\uf578"
    ], [
        u"\uf583",
        u"\uf583",
        u"\uf586",
        u"\uf587",
        u"\uf587",
        u"\uf588",
        u"\uf588",
        u"\uf589",
        u"\uf58a",
        u"\uf584"
    ],
]

capacity = subprocess.run(
    [
        "cat", 
        "/sys/class/power_supply/BAT1/capacity"
    ],
    stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

power_now = subprocess.run(
    [
        "cat",
        "/sys/class/power_supply/BAT1/power_now"
    ],
    stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

icon_x = 1 if power_now == 0 else 0
icon_y = round(int(capacity) / 10)
icon = icons[icon_x][icon_y]

print(f"{capacity}% {icon}")
