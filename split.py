#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os

#os.system('find ../../../h/Videos/Recording/Gopro/* -maxdepth 3 | grep -i ".mp4">list.txt')
file_list = []
for root, dirs, files in os.walk("./"):
    for fn in files:
        filepath = os.path.join(root, fn)
        if fn.endswith(".mp4") or fn.endswith(".MP4"):
            file_list.append(filepath)


for f in file_list:
    s = os.path.getsize(f)
    if s < 1500000000:
        continue
    cmd = "mp4box -splits 1500000 " + "\"" + f + "\""
    print cmd
    os.system(cmd)