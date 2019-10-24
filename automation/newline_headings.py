#! /usr/bin/env python
from functions import get_state
import re

state = get_state()

def get_formatted_file(lines):
    code_lines = []
    code_block = False
    for index, line in enumerate(lines):
        if code_block:
            if line.startswith("```"):
                code_block = False    
            code_lines.append(index)
            continue
        if line.startswith("```"):
            code_block = True
            code_lines.append(index)

    previous_line = ""
    newlines_to_add = []
    for index, line in enumerate(lines):
        if index in code_lines:
            previous_line = line
            continue
        if line.startswith("#") and previous_line != "\n" and index != 0:
            newlines_to_add.append(index)
        previous_line = line

    for newline in newlines_to_add:
        lines[newline] = "\n" + lines[newline] 

    return "".join(lines)

for topic in state["topics"]:
    for module in topic["modules"]:
        formatted_file = ""
        with open(module["gitUri"] + "/README.md", "r") as file:
            formatted_file = get_formatted_file(file.readlines())
        with open(module["gitUri"] + "/README.md", "w") as file:
            file.write(formatted_file)
            
