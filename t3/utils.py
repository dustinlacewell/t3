import os
import fnmatch
import subprocess

import pkg_resources

from jinja2 import Environment


def shell(command):
    return subprocess.check_output(command, shell=True)


def ensure_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_resource_path(path):
    full_path = 'resources/{}'.format(path)
    return pkg_resources.resource_filename('t3', full_path)


def read_resource(path):
    filename = get_resource_path(path)
    with open(filename) as fobj:
        return fobj.read()


def find_files(path, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def find_in_files(files, needle):
    for filename in files:
        with open(filename) as fobj:
            lineno = 0
            for line in fobj:
                if needle in line:
                    yield filename, lineno
                lineno += 1


def get_template(path):
    content = read_resource(path)
    return Environment().from_string(content)


def render_template(path, context):
    template = get_template(path)
    return template.render(context)


def find_makefile(html=False):
    for filename in os.listdir(os.getcwd()):
        if not filename.endswith('.t3m'):
            continue
        if html and 'html' not in filename:
            continue
        return filename


def read_makefile():
    filename = find_makefile()
    with open(filename) as fobj:
        makefile = {'html': False}
        for line in fobj:
            line = line.decode('utf-8')
            if line.startswith('-Fy'):
                _, makefile['obj_path'] = line.split(" ", 1)
            elif line.startswith('-o'):
                _, makefile['img_file'] = line.split(" ", 1)
            elif 'adv3web' in line:
                makefile['html'] = False
