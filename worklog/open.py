import argparse
import subprocess

import frontmatter
from worklog import config

parser = argparse.ArgumentParser()
parser.add_argument("path")


def main():
    args = parser.parse_args()

    TARGET = config.WORKLOG_DIR / args.path

    if not TARGET.exists():
        # Drop extension and use the rest of the file as our date
        date, ext = args.path.split(".")

        with open("template.markdown") as fp:
            TEMPLATE = fp.read()

        TEMPLATE = TEMPLATE.replace("<date>", date)
        post = frontmatter.loads(TEMPLATE)
        post["date"] = date

        with TARGET.open("w+") as fp:
            fp.write(frontmatter.dumps(post))

    subprocess.call(["/usr/bin/open", TARGET])
