# topalias

[![Build Status](https://travis-ci.com/CSRedRat/topalias.svg?branch=master)](https://travis-ci.com/CSRedRat/topalias)
[![Coverage](https://coveralls.io/repos/github/CSRedRat/topalias/badge.svg?branch=master)](https://coveralls.io/github/CSRedRat/topalias?branch=master)
[![Python Version](https://img.shields.io/pypi/pyversions/topalias.svg)](https://pypi.org/project/topalias/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Linux bash alias generator


## Features

- Generate short alias for popular command from bash history
- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Installation

```bash
pip install topalias
```

From source:
```bash
git clone https://github.com/CSRedRat/topalias
python topalias/setup.py install
```

## Example

Showcase how your project can be used:

```bash
topalias # check if you uses aliases in ~/.bash_aliases - analyze and print usage statistics, offers to find new simple aliases
topalias -h # print help
topalias history # analyze local bash history
topalias h --min=2 # set minimal lenght for generated acronym filter, so that exclude some short command and find long, hard, usable command
```

File path search order:
- .bash_history in current . directory
- .bash_history in home ~ directory
- example development files in topalias/data

## License

[GPLv3](https://github.com/CSRedRat/topalias/blob/master/LICENSE)
