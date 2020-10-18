# -*- coding: utf-8 -*-
"""Main python file for start project execution (entrypoint). Functions are listed in topalias.py and other modules"""

import cli
import topalias

if __name__ == "__main__":
    topalias.welcome("start as module: python -m topalias")
    cli.main()
