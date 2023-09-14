#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filen = 'add_item.json'

try:
    con = load_from_json_file(filen)
except:
    con = []
for i in range(1, len(sys.argv)):
    con.append(sys.argv[i])

save_to_json_file(con, filen)
