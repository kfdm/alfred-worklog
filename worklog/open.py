import os
import subprocess
import sys

from worklog import config

TARGET = os.path.join(config.WORKLOG_DIR, sys.argv[1])


def main():
    with open("template.markdown") as fp:
        TEMPLATE = fp.read()

    if not os.path.exists(TARGET):
        DATE = sys.argv[1].split("-")
        TEMPLATE = TEMPLATE.replace("<date>", "{}-{}-{}".format(*DATE))
        with open(TARGET, "w+") as fp:
            fp.write(TEMPLATE)

    subprocess.call(["/usr/bin/open", TARGET])
