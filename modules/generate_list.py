from os import system as term

def scan(target, type, all):
    target = f'"{target}"'
    if all:
        term(f'ls {target}/*.mp4 {target}/*.mov {target}/*.avi {target}/*.mkv {target}/*.mpg {target}/*.mpeg 2> /dev/null | xargs -I file ffprobe -i file -show_entries format=duration -v quiet -of csv="p=0" > .list.tmp')
    else:
        term(f'ls {target}/*.{type} 2> /dev/null | xargs -I file ffprobe -i file -show_entries format=duration -v quiet -of csv="p=0" > .list.tmp')
