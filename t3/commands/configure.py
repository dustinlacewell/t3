# -*- coding: utf-8 -*-
import os
import json

import click

from t3 import utils


def find_sources(path):
    return utils.find_files(path, '*.t')


def find_version_info(sources):
    info = {}
    results = list(utils.find_in_files(sources, 'versionInfo'))
    if len(results):
        filename, location = results[0]
        with open(filename) as fobj:
            lineno = 0
            for line in fobj:
                if lineno >= location:

                    if line[:1] in ['}', ';']:
                        break

                    if '=' in line:
                        key, value = [x.strip() for x in line.split('=', 1)]
                        if key in ['name', 'byline', 'desck']:
                            info[key] = value.strip('\'"')

                lineno += 1
    return info


@click.command()
@click.option('-s', '--src-path', default='src')
@click.option('-d', '--dst-path', default='build')
@click.option('-h', '--html', is_flag=True)
def configure(src_path, dst_path, html):
    """Configure a TADS3 makefile."""
    sources = find_sources(src_path)
    info = find_version_info(sources)

    bin_path = os.path.join(dst_path, 'bin')
    obj_path = os.path.join(dst_path, 'obj')

    gamename = info.get('name', 'game')
    basename = gamename.replace(' ', '_').lower()

    if html:
        obj_path += "_html"
        basename += "_html"

    make_filename = basename + ".t3m"
    game_filename = basename + ".t3"
    game_filename = os.path.join(bin_path, game_filename)

    context = {
        'game_name': info.get('name', 'game'),
        'game_author': info.get('byline', 'Anon'),
        'game_desc': info.get('desc', 'A nondescript game.'),
        'dst_path': dst_path,
        'obj_path': obj_path,
        'img_file': game_filename,
        'makefile': make_filename,
        'sources': sources,
        'html': html,
        'debug': False,
    }
    makefile = utils.render_template("makefile.jinja2", context)


    with open(make_filename, 'w') as fobj:
        fobj.write(makefile)

    with open("makefile.json", 'w') as fobj:
        json.dump(context, fobj)

    return 0
