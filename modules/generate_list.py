from os import system as term

def scan(target, type, all, subs):
    if subs:
        term ('ls -d1 */ > .dirlist.tmp')
        with open ('.dirlist.tmp') as dls:
            for dir in dls:
                dir = dir.strip()
                if all:
                    term(f'ls "{target}/{dir}" | grep -E "\\.mp4|\\.mkv|\\.mov|\\.mpg|\\.mpeg|\\.avi" | cat /dev/stdin | xargs -I filename echo "{dir}"filename >> .lst.tmp')
                else:
                    term(f'ls -R {target} | grep -E "\\.{type}" 2> /dev/null | cp /dev/stdin .lst.tmp')
        # exit()
    else:
        target = f"'{target}'"
        if all:
            term(f'ls {target}/*.mp4 {target}/*.mov {target}/*.avi {target}/*.mkv {target}/*.mpg {target}/*.mpeg 2> /dev/null | cp /dev/stdin .lst.tmp')
        else:
            term(f'ls {target}/*.{type} 2> /dev/null | cp /dev/stdin .lst.tmp')
    
