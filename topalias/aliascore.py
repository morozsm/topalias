# -*- coding: utf-8 -*-
"""Main function module. Not for executing, only library. Run project from __init__.py"""

import os
import random
import re
from collections import defaultdict

home = os.path.expanduser("~")
PATHS = (".", home)
NOTHING = "Empty"


def find_first(filename: str, paths: tuple) -> str:  # type: ignore
    """Find file in PATH
    :rtype: str
    :param filename: what file search
    :param paths: where search file with directory order
    :type filename: str
    :type paths: list
    """
    for directory in paths:
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            return full_path
    return NOTHING


def find_history() -> str:
    """Find command history file"""
    history_name: str = ".bash_history"
    path = find_first(history_name, PATHS)
    if path != NOTHING:
        return path
    print("File {} not found in any of the directories".format(history_name))
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    data_path = os.path.join(file_dir, r"topalias/data/.bash_history")
    return data_path  # noqa: WPS331


def find_aliases() -> str:
    """Find defined aliases file for shell"""
    aliases_name = ".bash_aliases"
    path = find_first(aliases_name, PATHS)
    if path != NOTHING:
        return path
    print("File {} not found in any of the directories".format(aliases_name))
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    data_path = os.path.join(file_dir, r"topalias/data/.bash_aliases")
    return data_path  # noqa: WPS331


def top_command(command, top=20) -> list:  # type: ignore
    """List top executed command from history"""
    counts = defaultdict(int)  # type: ignore
    for x in command:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


def top_alias():
    """Top used aliases"""
    print("Top used aliases: ")
    print("For suggest new amazing short aliases run:\ntopalias h")
    print("Print help:\ntopalias -h")


acronymize = re.compile(r"(?:(?<=\s)|^)(?:[a-z]|\d+)")


def welcome(event: str) -> None:
    """Event message inside the program."""
    print(f"console util {event}")


def filter_alias_length(raw_command_bank, min_length: int) -> list:  # type: ignore
    """Return acronyms with minimal length"""
    filtered_bank = []
    for command in raw_command_bank:
        gen_alias = "".join(acronymize.findall(command))
        if len(gen_alias) >= min_length:
            filtered_bank.append(command)
        else:
            print(f"COMMAND_FILTERED: {command}")

    return filtered_bank


def print_stat(raw_lines, filtered) -> None:
    """Any statistics"""
    rows_count = len(raw_lines)
    unique_count = len(set(raw_lines))
    filtered_count = unique_count - len(set(filtered))
    return print(
        f"commands in history: {rows_count}, unique commands: {unique_count}, filtered by length: {filtered_count}",
    )


HISTTIMEFORMAT_FIRST = "Hint (usability): add timestamp to new history: "
HISTTIMEFORMAT_SECOND = (
    "echo \"export HISTTIMEFORMAT='%F %T '\" >> ~/.bashrc"  # noqa: WPS323
)
HISTTIMEFORMAT = "".join((HISTTIMEFORMAT_FIRST, HISTTIMEFORMAT_SECOND))

hint_bank = (
    "Hint (secure): Add space ' ' before sensitive command in terminal for skip save current command in history!",
    "Hint: command 'sudo !!' after you forget add sudo before command in previous command",
    "Hint: command !<history command number> for repeat command from history",
    HISTTIMEFORMAT,
    "Hint (usability): ignore command in history: echo \"export HISTIGNORE='ls -l:pwd:date:ll:ls:'\" >> ~/.bashrc",
    'Hint (usability): ignore duplicates in history: echo "export HISTCONTROL=ignoreboth" >> ~/.bashrc',
)


def print_hint() -> None:
    """Hints for user"""
    print("\nRun after add alias: source ~/.bash_aliases\n")
    print(random.choice(hint_bank))


def print_history(acronym_length) -> None:  # noqa: WPS210
    """Main function for print top commands and suggestions aliases"""
    command_bank = []
    with open(find_history(), "r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("#", 0, 1):
                s = line.rstrip()
                command_bank.append(s)
                # print("".join(r.findall(s)))  # noqa: E800
            # l.append(line.split('#')[0].split())  # noqa: E800
    filtered_alias_bank = filter_alias_length(command_bank, acronym_length)
    top_raw_list = top_command(filtered_alias_bank)
    print("\n")

    for num, ranked_command in reversed(list(enumerate(top_raw_list, start=1))):
        acronym = "".join(acronymize.findall(ranked_command[0]))
        linux_add_alias = (
            f"echo \"alias {acronym}='{ranked_command[0]}'\" >> ~/.bash_aliases"
        )
        print(
            f"{num}. {ranked_command[0]}\n",  # noqa: WPS221
            f"executed count: {ranked_command[1]}, suggestion: {acronym}",
            "\n",
            f"{linux_add_alias}",
        )
    print_stat(command_bank, filtered_alias_bank)
    print_hint()
