# topalias
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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
pip3 install -U --user topalias
```

From source:
```bash
git clone https://github.com/CSRedRat/topalias
python3 topalias/setup.py install
```

## Example

Showcase how your project can be used:

```bash
topalias # check if you uses aliases in ~/.bash_aliases - analyze and print usage statistics, offers to find new simple aliases
topalias -h # print help
topalias history # analyze local bash history
topalias h --min=2 # set minimal length for generated acronym filter, so that exclude some short command and find long, hard, usable command
```

File path search order:
- .bash_history in current . directory
- .bash_history in home ~ directory
- example development files in topalias/data

Run as python module:
```bash
python3 -m topalias
```

Run as python script without install:
```bash
git clone https://github.com/CSRedRat/topalias
python3 topalias/topalias/cli.py -h
```

## License

[GPLv3](https://github.com/CSRedRat/topalias/blob/master/LICENSE)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://metin2wiki.ru/"><img src="https://avatars1.githubusercontent.com/u/1287586?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sergey Chudakov</b></sub></a><br /><a href="https://github.com/CSRedRat/topalias/commits?author=CSRedRat" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!