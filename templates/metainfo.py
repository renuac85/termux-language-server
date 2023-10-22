"""This file is generated by scikit-build.generate.
The information comes from pyproject.toml.
It provide some metainfo for docs/conf.py to build documents and
help2man to build man pages.
"""
from datetime import datetime

# For docs/conf.py
project = "$name"
author = "\n".join(f"{a[0]} <{a[1]}>" for a in $authors)
copyright = datetime.now().year

# For help2man
DESCRIPTION = "$description"
EPILOG = "Report bugs to " + $urls["Bug Report"]
VERSION = f"""$name $version
Copyright (C) {copyright}
Written by {author}"""
