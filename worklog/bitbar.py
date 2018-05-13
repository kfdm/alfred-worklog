import collections
import datetime
import glob
import logging
import os
import sys

WORKLOG_GLOB = os.path.expanduser('~/Documents/worklog/*.markdown')

if 'BitBar' not in os.environ:
    logging.basicConfig(level=logging.DEBUG)
else:
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8')


class Worklog(object):
    def __init__(self, path):
        self.path = path
        self.sections = collections.defaultdict(list)

    def __enter__(self):
        with open(self.path, encoding='utf8') as fp:
            in_frontmatter = False
            in_section = None
            for line in fp.readlines():
                line = line.strip()
                if not line:
                    continue
                if line == '---' and in_frontmatter:
                    in_frontmatter = False
                    continue
                if line == '---' and not in_frontmatter:
                    in_frontmatter = True
                    continue
                if in_frontmatter:
                    continue
                if line.startswith('#'):
                    in_section = line.lstrip('#').lstrip(' ')
                if line.startswith('*') and in_section:
                    entry = line.lstrip('*').lstrip(' ')
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

    for file in sorted(glob.glob(WORKLOG_GLOB), reverse=True)[:10]:
        with Worklog(file) as wl:
            print(wl.date.strftime('%A, %B %d'))
            for section, entries in wl:
                if entries:
                    print('--', section)
                    for entry in entries:
                        print('---- ', entry)
            print('-----')
            print('-- open | bash="open ' + file + '"')
