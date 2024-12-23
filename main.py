#!/usr/bin/env python
from modules import cli_system, generate_list, get_length
print ("Get Length for Linux, based on ffmeg, Developed by Hannibal\nhttps://github.com/theHannibalist")

# Starts the commandline interface and gets the arguments
args = cli_system.run_parser()

# Generates a temporary file containing files list and their length
generate_list.scan(args['target'], args['type'], args['all'])

# Reads the temporary file list and calculates the total length
get_length.show_final()



