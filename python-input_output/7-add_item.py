#!/usr/bin/python3
"""
This module when run adds all arguments to a python list
and save them to a file
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []

for i in range(1, len(sys.argv)):
    obj.append(sys.argv[i])

save_to_json_file(obj, "add_item.json")
