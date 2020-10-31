# -*- coding: utf-8 -*-
"""Main python file for start project execution (entrypoint). Functions are listed in aliascore.py and other modules"""

import aliascore as core
import cli as cli

if __name__ == "__main__":
    core.welcome("start as module: python -m topalias")
    cli.cli()
