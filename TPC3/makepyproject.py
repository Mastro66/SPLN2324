#!/usr/bin/env python3
"""
python3 makepyproject.py
"""

import jjcli
import jinja2
from glob import glob
import os
import json

__version__ = "0.0.1"

def main():
    mods = glob("*.py")
    if len(mods) >= 1:
        name = mods[0].replace(".py", "")
    else:
        name = input("Modulo?")

    version = jjcli.qx(f"grep __version__ {name}.py")
    print(version)

    pp = jinja2.Template("""
    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{name}}"
    authors = [
        {name = "{{author}}", email = "{{email}}"}, number = "{{number}}",
    ]
    version = "0.0.1"

    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.8"
    dynamic = [ "description"]

    dependencies = [
        "jjcli",
        "jinja2"
    ]

    [project.scripts]
    {{name}} = "{{name}}:main"
    """)

    metadata_path = "METADATA.json"
    
    # Check if the METADATA.json file exists
    if not os.path.exists(metadata_path):
        print("Error: METADATA.json not found.")
        return
    
    # Load metadata from METADATA.json
    with open(metadata_path, 'r') as file:
        data = json.load(file)
        author = data.get("Username", "")
        email = data.get("Email", "")
        number = data.get("Number", "")

    out = pp.render({"name": name, "author": author, "email": email, "number":number})
    print("DEBUG:", out)

    # Write generated output to pyproject.toml
    with open("pyproject.toml", "w") as file_output:
        file_output.write(out)

if __name__ == "__main__":
    main()
