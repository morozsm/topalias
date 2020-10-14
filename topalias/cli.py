# -*- coding: utf-8 -*-
"""Console script for topalias."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for topalias."""
    click.echo("topalias - linux bash/zsh alias generator & history analytics https://github.com/CSRedRat/topalias")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
