#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Console script for topalias."""

import sys

import click

import aliascore as core


class AliasedGroup(click.Group):
    """Add alias for command by function name"""

    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)


@click.group(
    cls=AliasedGroup,
    context_settings=dict(help_option_names=["-h", "--help"]),
    invoke_without_command=True,
)
@click.pass_context
def cli(ctx) -> int:
    """Entrypoint function, group command"""
    if ctx.invoked_subcommand is None:
        main()
    return 0


@cli.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
)
def main() -> int:
    """Print bash history file."""
    click.echo(
        "topalias - linux bash/zsh alias generator & history analytics https://github.com/CSRedRat/topalias",
    )
    if not core.find_aliases():
        top_history()  # pylint: disable=no-value-for-parameter
    else:
        core.top_alias()
        top_history()  # pylint: disable=no-value-for-parameter
    return 0


@cli.command(name="history")
@click.option("--acr", default=1, help="Will print alias not less than this.")
def top_history(acr) -> int:
    """Print bash history file."""
    click.echo(
        core.print_history(acr),
    )
    return 0


ALIASES = {
    "h": top_history,
}

if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover # pylint: disable=no-value-for-parameter
