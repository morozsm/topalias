# -*- coding: utf-8 -*-
"""Top-level package for topalias."""

__author__ = "Sergey Chudakov"
__email__ = "csredrat@gmail.com"
__version__ = "2.0.1"

import json
import os
import sys

import requests
from packaging.version import parse  # noqa: WPS347

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__))),
)  # noqa: WPS221
# isort: split  # noqa: E800

# pylint: disable=wrong-import-position
# for . import *
# pylint: enable=wrong-import-position

TOPALIAS_PYPI_LATEST_VERSION = "https://pypi.python.org/pypi/topalias/json"

TOPALIAS_EXAMPLES = "https://raw.githubusercontent.com/CSRedRat/topalias/master/topalias/data/.bash_aliases"


def get_version(url=TOPALIAS_PYPI_LATEST_VERSION):
    """Return version of topalias package on pypi.org."""
    req = requests.get(url)
    version = parse("0")
    if req.status_code == requests.codes.ok:  # pylint: disable=no-member
        req.encoding = req.apparent_encoding
        j = json.loads(req.text.encode(req.encoding))
        releases = j.get("releases", [])
        for release in releases:
            ver = parse(release)
            if not ver.is_prerelease:
                version = max(version, ver)
    return version


def get_examples(url=TOPALIAS_EXAMPLES):
    """Give dynamic .bash_aliases example from GitHub."""
    req = requests.get(url)
    alias_examples = ""
    if req.status_code == requests.codes.ok:  # pylint: disable=no-member
        req.encoding = req.apparent_encoding
        alias_examples = req.text
    return alias_examples
