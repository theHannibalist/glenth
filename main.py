#!/usr/bin/env python

print ("Get Length for Linux, based on ffmeg, Developed by Lenesis")

from os import system as term

term('ls *.mp4 *.mov *.avi *.mkv *.mpg *.mpeg 2> /dev/null 2> /dev/null | xargs -I file ffprobe -i file -show_entries format=duration -v quiet -of csv="p=0" > .list.tmp')
with open('.list.tmp') as f:
    i = 0
    for line in f:
        i += float(line)

    hr = int(float(i / 60 / 60))
    mn = int(( i /60) % 60)
    print (f"total {hr} hours and {mn} minutes")
term ('rm .list.tmp')

