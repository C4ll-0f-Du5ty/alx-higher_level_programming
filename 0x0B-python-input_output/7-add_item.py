#!/usr/bin/python3
"""adding all arguments to a Python list"""


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
import sys
import os

filenamedest = 'add_item.json'

if os.path.isfile(filenamedest):
    pack = load(filenamedest)
else:
    pack = []
pack.extend(sys.argv[1:])
save(pack, 'add_item.json')
