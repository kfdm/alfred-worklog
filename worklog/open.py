import argparse
import os
import subprocess

from worklog import config

parser = argparse.ArgumentParser()
parser.add_argument("path")


def main():
    args = parser.parse_args()

    TARGET = os.path.join(config.WORKLOG_DIR, args.path)

    if not os.path.exists(TARGET):
        with open("template.markdown") as fp:
            TEMPLATE = fp.read()

        DATE = args.path.split("-")
        TEMPLATE = TEMPLATE.replace("<date>", "{}-{}-{}".format(*DATE))
        with open(TARGET, "w+") as fp:
            fp.write(TEMPLATE)

    subprocess.call(["/usr/bin/open", TARGET])
