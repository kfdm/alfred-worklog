import argparse
import os

import frontmatter
from worklog.bitbar import Worklog


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("dest")
    args = parser.parse_args()

    for fn in os.listdir(args.source):
        if not fn.endswith("markdown"):
            continue

        old_path = os.path.join(args.source, fn)
        year, month, day, _ = fn.split("-", 3)
        date = "{}-{}-{}".format(year, month, day)
        new_path = os.path.join(args.dest, date + ".markdown")

        with open(old_path) as fp:
            print('importing', old_path)
            wl = frontmatter.load(fp)
            # Remove jekyll specific
            wl.metadata.pop("layout", False)
            # Explicitly set date
            wl.metadata.setdefault("date", date)
        with open(new_path, "w+") as fp:
            fp.write(frontmatter.dumps(wl))
