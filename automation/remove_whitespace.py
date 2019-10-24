#! /usr/bin/env python
from pathlib import Path
import re

readme_file_paths = list(Path("topics").glob("**/README.md"))
for file_path in readme_file_paths:
    contents = ""
    with open(file_path, "r") as file:
        contents = file.read()
    with open(file_path, "w") as file:
        file.write(contents.replace("\n\n\n", "\n\n"))

