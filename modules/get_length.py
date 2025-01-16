from os import system as term
from modules import conv
def show_final():
    with open('.lst.tmp') as f:
        i = 0
        for line in f:
            # print (line.strip())
            for item in line.split():
                term (f'ffprobe -i {item} -show_entries format=duration -v quiet -of csv="p=0" > .timelist.tmp')
                with open ('.timelist.tmp') as t:
                    for time in t :
                        i += float(time)
                        print (f'\033[33m*\033[39m {item} ===> \033[33m{conv.ert(time)['hr']} hours \033[39mand \033[33m{conv.ert(time)['mn']} minutes\033[39m\n')
        
            


        print (f"total:\n\033[33m {conv.ert(i)['hr']} hours\033[39m and\033[33m {conv.ert(i)['mn']} minutes\033[39m")
        term ('rm .lst.tmp .timelist.tmp')
