import argparse
import datetime
import subprocess

import frontmatter
from worklog import config

TODAY = datetime.datetime.today()

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=config.fromdt(TODAY))


def main():
    args = parser.parse_args()

    TARGET = config.WORKLOG_DIR / args.path

    if not TARGET.exists():
        # Drop extension and use the rest of the file as our date
        date, ext = TARGET.name.split(".")

        with open("template.markdown") as fp:
            TEMPLATE = fp.read()

        TEMPLATE = TEMPLATE.replace("<date>", date)
        post = frontmatter.loads(TEMPLATE)
        post["date"] = date

        with TARGET.open("w+") as fp:
            fp.write(frontmatter.dumps(post))

    subprocess.call(["/usr/bin/open", TARGET])
