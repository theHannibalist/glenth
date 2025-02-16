from os import system as term
from modules import conv
def show_final():
    with open('.lst.tmp') as f:
        i = 0
        for line in f:
            line = line.strip()
            term (f'ffprobe -i "{line}" -show_entries format=duration -v quiet -of csv="p=0" > .timelist.tmp')
            with open ('.timelist.tmp') as t:
                for time in t :
                    i += float(time)
                    hrs = conv.ert(time)['hr']
                    mns = conv.ert(time)['mn']
                    print (f'\033[33m*\033[39m {line} ===> \033[33m{hrs} hours \033[39mand \033[33m{mns} minutes\033[39m\n')
        
            # for item in line.split():
                # print (item)
                # exit()
                # term (f'ffprobe -i {item} -show_entries format=duration -v quiet -of csv="p=0" > .timelist.tmp')
                # with open ('.timelist.tmp') as t:
                #     for time in t :
                #         i += float(time)
                #         print (f'\033[33m*\033[39m {item} ===> \033[33m{conv.ert(time)['hr']} hours \033[39mand \033[33m{conv.ert(time)['mn']} minutes\033[39m\n')
        
            

        hrs = conv.ert(i)['hr']
        mns = conv.ert(i)['mn']
        print (f"total:\n\033[32m {hrs} hours\033[39m and\033[32m {mns} minutes\033[39m")
        term ('rm .lst.tmp .timelist.tmp .dirlist.tmp 2> /dev/null')
