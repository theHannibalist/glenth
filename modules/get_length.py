from os import system as term

def show_final():
    with open('.list.tmp') as f:
        i = 0
        for line in f:
            i += float(line)

        hr = int(float(i / 60 / 60))
        mn = int(( i /60) % 60)
        print (f"total\033[33m {hr} hours\033[39m and\033[33m {mn} minutes\033[39m")
        term ('rm .list.tmp')
