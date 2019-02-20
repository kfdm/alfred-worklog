import collections
import datetime
import json
import os

from worklog import config

RESPONSE = []
TODAY = datetime.datetime.today()
TOMORROW = TODAY + datetime.timedelta(days=1)
YESTERDAY = TODAY - datetime.timedelta(days=1)


SPECIAL = collections.OrderedDict()

SPECIAL[TODAY.strftime(config.WORKLOG_FMT)] = {
    'title': 'Open Today for Editing',
}

SPECIAL[TOMORROW.strftime(config.WORKLOG_FMT)] = {
    'title': 'Open Tomorrow for Editing',
    'icon': {'path': 'tomorrow.png'},
}

SPECIAL[YESTERDAY.strftime(config.WORKLOG_FMT)] = {
    'title': 'Open Yesterday for Editing',
    'icon': {'path': 'yesterday.png'},
}

FILES = [f for f in os.listdir(config.WORKLOG_DIR) if f.endswith('markdown')]


def main():
    for ts, args in SPECIAL.items():
        args['arg'] = ts
        RESPONSE.append(args)

    for path in sorted(FILES, reverse=True)[:8]:
        if path not in SPECIAL:
            RESPONSE.append({
                'title': os.path.basename(path),
                'arg': path,
                'icon': {'path': 'review.png'},
            })

    print(json.dumps({'items': RESPONSE}))
