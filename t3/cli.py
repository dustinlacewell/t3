# -*- coding: utf-8 -*-

"""Console script for t3."""
import sys
import click


from t3.commands.configure import configure
from t3.commands.make import make
from t3.commands.clean import clean


@click.group()
def main(args=None):
    """Console script for t3."""
    # with click.Context(main) as ctx:
    #     click.echo(main.get_help(ctx))
    return 0


main.add_command(configure)
main.add_command(make)
main.add_command(clean)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
