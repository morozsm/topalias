# -*- coding: utf-8 -*-
"""Main python file for start project execution (entrypoint). Functions are listed in aliascore.py and other modules"""

import sys
import os

sys.path.append(os.getcwd())
# isort: split

# pylint: disable=wrong-import-position
import aliascore
import cli

# pylint: enable=wrong-import-position


if __name__ == "__main__":
    aliascore.welcome("start as module: python -m topalias")
    cli.cli()  # pylint: disable=no-value-for-parameter
