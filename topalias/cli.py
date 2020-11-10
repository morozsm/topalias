#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Console script topalias."""

import sys

import aliascore as core
import click
from __init__ import __version__, get_version


class AliasedGroup(click.Group):
    """Add alias for command by function name"""

    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass  # noqa: WPS420
        return super().get_command(ctx, cmd_name)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"topalias utility version: {__version__}")
    click.echo(
        f"Latest release: {get_version()} on https://pypi.org/project/topalias/\n"
    )
    click.echo("Update command:\npip3 install -U --user topalias")
    ctx.exit()


@click.group(
    cls=AliasedGroup,
    context_settings=dict(help_option_names=["-h", "--help"]),  # noqa: C408
    invoke_without_command=True,
)
@click.option(
    "--min",
    "-l",
    "acr",
    default=1,
    type=int,
    help="Print alias acronym not less that value. Default: 1",
)
@click.option(
    "--count",
    "-c",
    default=20,
    type=int,
    help="Print specified number acronym suggestions. Default: 20",
)
@click.option(
    "--path",
    "-f",
    type=str,
    help="Change custom directory for files: .bash_aliases, .bash_history, .zsh_history",
)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Print current program version and check latest on pypi.org.",
)
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable debug strings in output.",
)
@click.pass_context
def cli(ctx, debug, acr, path, count) -> int:
    """See documentation and usage examples: https://csredrat.github.io/topalias"""

    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = core.debug = debug
    ctx.obj["acronym_minimal_length"] = acr
    ctx.obj["suggestion_count"] = count
    core.suggestion_count = ctx.obj["suggestion_count"]

    if path is not None:
        print(path)
        core.path.insert(0, path)

    if debug:
        click.echo("Debug mode is ON")
    if ctx.invoked_subcommand is None:
        return ctx.invoke(main)
    return 0


@cli.command(
    context_settings=dict(help_option_names=["-h", "--help"]),  # noqa: C408
)
@click.pass_context
def main(ctx) -> int:
    """Main function for group command call."""
    click.echo(
        "topalias - linux bash/zsh alias generator & history analytics https://github.com/CSRedRat/topalias",
    )
    if ctx.obj["DEBUG"]:
        click.echo(ctx.obj)

    if core.find_aliases():
        # core.top_alias()
        ctx.forward(top_history)  # pylint: disable=no-value-for-parameter
    else:
        ctx.forward(top_history)  # pylint: disable=no-value-for-parameter
    return 0


@click.command()
def version() -> None:
    print_version()


@cli.command(name="history")
@click.pass_context
def top_history(ctx) -> None:
    """Print bash history file."""
    if ctx.obj["DEBUG"]:
        click.echo(ctx.obj)

    acronym_minimal_length = ctx.obj["acronym_minimal_length"]

    if acronym_minimal_length is None:
        acronym_minimal_length = 1

    click.echo(
        core.print_history(acronym_minimal_length),
    )


ALIASES = {  # noqa: WPS407, need frozendict
    "h": top_history,
}

if __name__ == "__main__":
    sys.exit(cli(obj={}))  # pragma: no cover # pylint: disable=no-value-for-parameter
