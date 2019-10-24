#! /usr/bin/env python
# generate a table of contents for every readme file
from pathlib import Path
from collections import Counter
import re

toc_start = "<!--TOC_START-->"
toc_end = "<!--TOC_END-->"
# get every readme file
readme_files = list(Path("topics").glob("**/README.md"))
readme_files.append("./README.md")
readme_files.append("./CONTRIBUTING.md")
for readme in readme_files:
    print(readme)
    headings = []
    with open(readme, "r") as file:
        lines = file.read().split("\n")
        code_block = False
        for line in lines:
            if line.startswith("```"):
                code_block = not code_block
            if not code_block and line.startswith("#") and line != "## Contents":
                headings.append(line)

    heading_links = []
    for heading in headings:
        # remove special characters
        heading_link = re.sub('[^A-Za-z0-9 ]+', '', heading.replace("#", "")).strip().lower().replace("#", "").replace(" ", "-")
        heading_links.append(heading_link)
    # get rid of title heading
    heading_links.pop(0)
    headings.pop(0)
    # add numbers to headings
    heading_duplicates = dict(Counter(heading_links))
    for duplicate_heading, count in heading_duplicates.items():
        if count > 1:
            x = 0
            for i, heading in enumerate(heading_links):
                if heading == duplicate_heading:
                    if x != 0:
                        heading_links[i] = heading + "-" + str(x)
                    x += 1
    toc = {}
    table_of_contents = "## Contents\n"
    for i, heading in enumerate(headings):
        depth = 0
        for letter in heading:
            if letter != "#":
                break
            depth += 1
        formatted_heading = heading.replace("#", "").strip()
        indent = ""
        for a in range(2, depth):
            indent = indent + "\t"
        entry = "[" + formatted_heading + "](#" + heading_links[i] + ")"
        table_of_contents = table_of_contents + indent + "- " + entry + "\n"
    readme_no_toc = ""
    in_toc = False
    for line in lines:
        if line == toc_start:
            in_toc = True
        if line == toc_end:
            in_toc = False
            continue
        if not in_toc:
            readme_no_toc = readme_no_toc + line + "\n"
    new_readme = ""
    heading_count = 0
    toc_added = False
    for line in readme_no_toc.split("\n"):
        if line.startswith("#"):
            heading_count += 1
        if heading_count == 2 and not toc_added:
            new_readme = new_readme + toc_start +  "\n" + table_of_contents + "\n" + toc_end + "\n"
            toc_added = True
        new_readme = new_readme + line + "\n"

    file = open(readme, "w")
    file.write(new_readme.strip() + "\n")
    file.close()

