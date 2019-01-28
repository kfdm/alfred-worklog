import collections
import datetime
import glob
import logging
import os
import sys
import re

import frontmatter

WORKLOG_GLOB = os.path.expanduser('~/Documents/worklog/*.markdown')

if 'BitBar' not in os.environ:
    logging.basicConfig(level=logging.DEBUG)
else:
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8')

MATCH_SECTION = re.compile("^[#]+\s(?P<section>.*)$")
MATCH_TODO = re.compile("^\s*[\*\-]\s+(?P<todo>.*)")


class Worklog(object):
    def __init__(self, path):
        self.path = path
        self.sections = collections.defaultdict(list)

    def __enter__(self):
        with open(self.path, encoding="utf8") as fp:
            post = frontmatter.load(fp)
            for line in post.content.split("\n"):
                line = line.strip()
                match = MATCH_SECTION.match(line)
                if match:
                    in_section = match.groups()[0]
                    continue

                match = MATCH_TODO.match(line)
                if match and in_section:
                    entry = match.groups()[0].strip()
                    if entry:
                        self.sections[in_section].append(entry)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        for section in self.sections:
            yield section, self.sections[section]

    @property
    def date(self):
        path = os.path.basename(self.path)
        year, month, day, _ = path.split('-')
        return datetime.date(int(year), int(month), int(day))


def main():
    print(':pencil:')
    print('---')
    print('RELOAD | refresh=true')
    print('---')

    later = []
    missed = []

    for file in sorted(glob.glob(WORKLOG_GLOB), reverse=True)[:10]:
        with Worklog(file) as wl:
            print(wl.date.strftime('%Y-%m-%d %A'))
            for section, entries in wl:
                if entries:
                    print('-- ', section, '| color=blue')
                    for entry in entries:
                        print('-- ', entry)
                        if section == 'Later':
                            later.append(wl.date.isoformat() + ' ' + entry)
                        if section == 'Goals' and not entry.endswith('~~'):
                            missed.append(wl.date.isoformat() + ' ' + entry)
            print('-----')
            print('-- open | bash="open ' + file + '"')

    if later:
        print('Later| color=blue')
        for entry in sorted(later):
            print('-- ', entry)
    if missed:
        print('Missed| color=red')
        for entry in sorted(missed):
            print('-- ', entry)
