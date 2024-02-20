#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys


save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

args = list(sys.argv[1:])

try:
    d = load_from_json("add_item.json")
except Exception:
    d = []

d.extend(args)

save_to_json(d, "add_item.json")
