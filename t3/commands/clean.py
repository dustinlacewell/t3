# -*- coding: utf-8 -*-
import os
import json
import shutil

import click


@click.command()
@click.option('-m', '--json-makefile', default='makefile.json')
@click.option('-a', '--all', is_flag=True)
def clean(json_makefile, all):
    """Remove build artifacts."""
    with open(json_makefile) as fobj:
        makefile = json.load(fobj)

    if os.path.exists(makefile['dst_path']):
        shutil.rmtree(makefile['dst_path'], True)

    if all:
        if os.path.exists(makefile['makefile']):
            os.remove(makefile['makefile'])

        if os.path.exists(json_makefile):
            os.remove(json_makefile)

    return 0
