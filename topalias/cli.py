#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Console script for topalias."""

import sys
import click

import aliascore as core


@click.group()
def cli():
    """Entrypoint function, group command"""
    pass


@click.command()
def main() -> int:  # args=None
    """Console script for topalias. Start util without arguments."""
    click.echo(
        "topalias - linux bash/zsh alias generator & history analytics https://github.com/CSRedRat/topalias",
    )
    return 0


@cli.command(name="print")
@click.option("--min", default=1, help="Will print alias not less than this.")
def print_history(min) -> int:  # args=None, @click.pass_context
    """Print bash history file."""
    click.echo(
        core.print_history(min),
    )
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
