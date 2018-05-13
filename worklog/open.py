#!/usr/bin/env python
import os
import subprocess
import sys

WORKLOG_DIR = os.path.join(os.path.expanduser('~'), 'Documents', 'worklog')
TARGET = os.path.join(WORKLOG_DIR, sys.argv[1])


def main():
    with open('template.markdown') as fp:
        TEMPLATE = fp.read()

    if not os.path.exists(TARGET):
        DATE = sys.argv[1].split('-')
        TEMPLATE = TEMPLATE.replace('<date>', '{}-{}-{}'.format(*DATE))
        with open(TARGET, 'w+') as fp:
            fp.write(TEMPLATE)

    subprocess.call(['/usr/bin/open', TARGET])
