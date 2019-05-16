import collections
import datetime
import glob
import logging
import os
import re
import sys
from operator import attrgetter

import frontmatter
from worklog import config

if "BitBar" not in os.environ:
    logging.basicConfig(level=logging.DEBUG)
else:
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf8")


class Section:
    example = "# Section Name"
    matcher = re.compile(r"^[#]+\s(?P<section>.*)$")


class Todo:
    @classmethod
    def match(cls, string):
        match = cls.matcher.match(string)
        if match:
            klass = cls()
            klass.body = match.groups()[0]
            return klass
        return None


class TodoPending(Todo):
    example = " - [ ] Pending TODO"
    matcher = re.compile(r"^\s*[\*\-]\s+\[ \]\s+(?P<todo>.*)$")

    def __str__(self):
        return "[ ] " + self.body


class TodoComplete(Todo):
    example = " - [x] Completed TODD"
    matcher = re.compile(r"^\s*[\*\-]\s+\[x\]\s+(?P<todo>.*)$")

    def __str__(self):
        return "[x] " + self.body


class TodoCanceled(Todo):
    example = " - [-] Canceled TODO"
    matcher = re.compile(r"^\s*[\*\-]\s+\[-\]\s+(?P<todo>.*)$")

    def __str__(self):
        return "[-] " + self.body


class TodoRescheduled(Todo):
    example = " - [>] Rescheduled TODO"
    matcher = re.compile(r"^\s*[\*\-]\s+\[>\]\s+(?P<todo>.*)$")

    def __str__(self):
        return "[>] " + self.body


class Worklog(object):
    def __init__(self, path):
        self.path = path
        self.sections = collections.defaultdict(list)

    def __enter__(self):
        with open(self.path, encoding="utf8") as fp:
            post = frontmatter.load(fp)
            for line in post.content.split("\n"):
                line = line.strip()
                match = Section.matcher.match(line)
                if match:
                    in_section = match.groups()[0]
                    continue

                for parser in [
                    TodoPending,
                    TodoComplete,
                    TodoCanceled,
                    TodoRescheduled,
                ]:
                    match = parser.match(line)
                    if match and in_section:
                        self.sections[in_section].append(match)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        for section in self.sections:
            yield section, self.sections[section]

    @property
    def date(self):
        path = os.path.basename(self.path)
        year, month, day = path.split(".")[0].split("-")
        return datetime.date(int(year), int(month), int(day))


sections = {
    TodoPending: "Later| color=red",
    TodoRescheduled: "Deferred| color=orange",
    TodoComplete: "Done| color=green",
}


def main():
    print(":pencil:")
    print("---")
    print("RELOAD | refresh=true")
    print("---")

    todos = collections.defaultdict(list)

    for fn in sorted(config.WORKLOG_GLOB, reverse=True)[:10]:
        with Worklog(fn) as wl:
            print(wl.date.strftime("%Y-%m-%d %A"))
            for section, entries in wl:
                if entries:
                    print("-- ", section, "| color=blue")
                    for entry in entries:
                        print("-- ", entry)
                        entry.date = wl.date
                        todos[type(entry)].append(entry)
            print("-----")
            print('-- open | bash="open %s" && exit' % fn)

    for klass, heading in sections.items():
        if todos[klass]:
            print(heading)
            for entry in sorted(todos[klass], key=attrgetter("date")):
                print("-- {} {}".format(entry.date.isoformat(), entry))
