# -*- coding: utf-8 -*-
"""Main function module. Not for executing, only library. Run project from __init__.py"""

import os

import re
from collections import defaultdict


PATHS = ['.', '~']


def find_first(filename, paths):
    for directory in paths:
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            return full_path

def find_history():
    history_name = '.bash_history'
    path = find_first(history_name, PATHS)
    if path:
        return path
    else:
        print("File {} not found in any of the directories".format(history_name))
        fileDir = os.path.dirname(os.path.realpath("__file__"))
        data_path = os.path.join(fileDir, "topalias\\data\\.bash_history")
        return data_path

def find_aliases():
    aliases_name = '.bash_aliases'
    path = find_first(aliases_name, PATHS)
    if path:
        return path
    else:
        print("File {} not found in any of the directories".format(aliases_name))


def top_command(command: list, top=20) -> list:
    counts = defaultdict(int)
    for x in command:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]

def top_alias():
    print("Top used aliases: ")
    print("For suggest new amazing short aliases run:\ntopalias h")
    print("Print help:\ntopalias -h")


r = re.compile(r"(?:(?<=\s)|^)(?:[a-z]|\d+)")


def welcome(event: str) -> None:
    """Event message inside the program."""
    print(f"console util {event}")


def filter_alias_length(raw_command_list: list, min_length: int) -> list:
    filtered_list = []
    for command in raw_command_list:
        gen_alias = "".join(r.findall(command))
        if len(gen_alias) >= min_length:
            filtered_list.append(command)
        else:
            print(f"COMMAND_FILTERED: {command}")

    return filtered_list


def print_stat(raw_lines, filtered):
    rows_count = len(raw_lines)
    unique_count = len(set(raw_lines))
    filtered_count = unique_count - len(set(filtered))
    # gen_count = # TODO
    return print(
        f"commands in history: {rows_count}, unique commands: {unique_count}, filtered by length: {filtered_count}"
    )


def print_history(alias_length) -> None:
    alias_bank = []
    with open(find_history(), "r") as f:
        for line in f:
            #print(str(line.startswith("#", 0, 1)) + " " + line)
            if not line.startswith("#", 0, 1):
                s = line.rstrip()
                alias_bank.append(s)
                #print("".join(r.findall(s)))
            # l.append(line.split('#')[0].split())
    # print(l)
    filtered_alias_bank = filter_alias_length(alias_bank, alias_length)
    top_raw_list = top_command(filtered_alias_bank)
    print(top_raw_list)
    for num, ranked_command in reversed(list(enumerate(top_raw_list, start=1))):
        gen_alias = "".join(r.findall(ranked_command[0]))
        linux_add_alias = f"alias {gen_alias}=\'{ranked_command[0]}\' >> ~/.bash_aliases"
        print(
            f"{num}. {ranked_command[0]}\n"
            f"executed count: {ranked_command[1]}, suggestion: {gen_alias}\n"
            f"{linux_add_alias}"
        )
    print_stat(alias_bank, filtered_alias_bank)
