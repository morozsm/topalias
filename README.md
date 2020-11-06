# topalias

[![Build Status](https://travis-ci.com/CSRedRat/topalias.svg?branch=master)](https://travis-ci.com/CSRedRat/topalias)
[![Coverage](https://coveralls.io/repos/github/CSRedRat/topalias/badge.svg?branch=master)](https://coveralls.io/github/CSRedRat/topalias?branch=master)
[![GitLab pipeline](https://gitlab.com/CSRedRat/topalias/badges/master/pipeline.svg)](https://gitlab.com/CSRedRat/topalias/-/pipelines)
[![Python Version](https://img.shields.io/pypi/pyversions/topalias.svg)](https://pypi.org/project/topalias/)

[topalias](https://github.com/CSRedRat/topalias) - Linux bash/zsh alias generator and statistics from command history, written on [Python](https://pypi.org/project/topalias/).


## Features

- Generate short alias for popular command from bash history
- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)


## Installation

From [pypi.org repository](https://pypi.org/project/topalias/):
```bash
pip3 install -U --user topalias
```

From source:
```bash
git clone https://github.com/CSRedRat/topalias
python3 topalias/setup.py install
```

## Example

![generated bash aliases](images/bash_screenshot.png "Bash topalias output")

Showcase how your project can be used:

```bash
topalias # check if you uses aliases in ~/.bash_aliases - analyze and print usage statistics, offers to find new simple aliases
topalias -h # print help
topalias history # analyze local bash history
topalias h --acr=2 # set minimal length for generated acronym filter, so that exclude some short command and find long, hard, usable command
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
    <td align="center"><a href="https://metin2wiki.ru/"><img src="https://avatars1.githubusercontent.com/u/1287586?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sergey Chudakov</b></sub></a><br /><a href="https://github.com/CSRedRat/topalias/commits?author=CSRedRat" title="Code">💻</a> <a href="#infra-CSRedRat" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-CSRedRat" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-CSRedRat" title="Maintenance">🚧</a> <a href="#platform-CSRedRat" title="Packaging/porting to new platform">📦</a> <a href="#mentoring-CSRedRat" title="Mentoring">🧑‍🏫</a> <a href="#example-CSRedRat" title="Examples">💡</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

*GitLab repository mirror with CI/CD: [https://gitlab.com/CSRedRat/topalias](https://gitlab.com/CSRedRat/topalias)*
