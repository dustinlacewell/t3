# -*- coding: utf-8 -*-
import os

import click

from t3 import utils


def filter_output(output):
    newlines = []
    for line in output.splitlines():
        line = line.decode('utf-8')
        if not line.startswith('<@>'):
            newlines.append(line)
    print('\n'.join(newlines))


@click.command()
@click.option('-a', '--rebuild-all', is_flag=True)
@click.option('-h', '--html', is_flag=True)
def make(rebuild_all, html):
    """Build a TADS3 makefile."""

    rebuild = '-a' if rebuild_all else ''

    output = utils.shell("t3make {} -f {}".format(rebuild, filename))
    filter_output(output)

    return 0
