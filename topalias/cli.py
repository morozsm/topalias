#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Console script for topalias."""

import sys

import aliascore as core
import click


class AliasedGroup(click.Group):
    """Add alias for command by function name"""

    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass  # noqa: WPS420
        return super().get_command(ctx, cmd_name)


@click.group(
    cls=AliasedGroup,
    context_settings=dict(help_option_names=["-h", "--help"]),  # noqa: C408
    invoke_without_command=True,
)
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable debug strings in output.",
)
@click.pass_context
def cli(ctx, debug) -> int:
    """Entrypoint function, group command"""
    if debug:
        click.echo("Debug mode is ON")
    if ctx.invoked_subcommand is None:
        return main()
    return 0


@cli.command(
    context_settings=dict(help_option_names=["-h", "--help"]),  # noqa: C408
)
def main() -> int:
    """Main function for group command call."""
    click.echo(
        "topalias - linux bash/zsh alias generator & history analytics https://github.com/CSRedRat/topalias",
    )
    if core.find_aliases():
        core.top_alias()
        top_history()  # pylint: disable=no-value-for-parameter
    else:
        top_history()  # pylint: disable=no-value-for-parameter
    return 0


@cli.command(name="history")
@click.option(
    "--acr",
    default=1,
    help="Will print acronyms for alias not less this value.",
)
def top_history(acr) -> None:
    """Print bash history file."""
    click.echo(
        core.print_history(acr),
    )


ALIASES = {  # noqa: WPS407, need frozendict
    "h": top_history,
}

if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover # pylint: disable=no-value-for-parameter
