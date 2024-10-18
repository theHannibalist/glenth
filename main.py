from os import system as term

term('ls *.mp4 | xargs -I file ffprobe -i file -show_entries format=duration -v quiet -of csv="p=0" > list.tmp')
with open('list.tmp') as f:
    i = 0
    for line in f:
        i += float(line)

    print(int(i / 60 / 60),'h')
term ('rm list.tmp')

