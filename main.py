#!/usr/bin/env python
from modules import cli_system, generate_list, get_length
print ("\033[36mGet Length\033[39m for \033[46m\033[30mLinux\033[39m\033[40m, based on \033[46m\033[30mffmpeg\033[39m\033[40m\nDeveloped by \033[32mHannibal\n\n\033[39m===[ \033[36mhttps://github.com/theHannibalist\033[39m ]===\n")

# Starts the commandline interface and gets the arguments
args = cli_system.run_parser()

# Generates a temporary file containing files list and their length
generate_list.scan(args['target'], args['type'], args['all'], args['subs'])

# Reads the temporary file list and calculates the total length
get_length.show_final()



