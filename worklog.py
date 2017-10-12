#!/usr/bin/env python
import os
import json
import datetime
import collections


RESPONSE = []
WORKLOG_DIR = os.path.join(os.path.expanduser('~'), 'Documents', 'worklog')
TODAY = datetime.datetime.today()
TOMORROW = TODAY + datetime.timedelta(days=1)
YESTERDAY = TODAY - datetime.timedelta(days=1)


SPECIAL = collections.OrderedDict()

SPECIAL[TODAY.strftime('%Y-%m-%d-%Y%m%d.markdown')] = {
    'title': 'Open Today for Editing',
    "icon": {'path': 'today.png'},
}

SPECIAL[TOMORROW.strftime('%Y-%m-%d-%Y%m%d.markdown')] = {
    'title': 'Open Tomorrow for Editing',
    "icon": {'path': 'tomorrow.png'},
}

SPECIAL[YESTERDAY.strftime('%Y-%m-%d-%Y%m%d.markdown')] = {
    'title': 'Open Yesterday for Editing',
    "icon": {'path': 'yesterday.png'},
}

FILES = [f for f in os.listdir(WORKLOG_DIR) if f.endswith('markdown')]


for ts, args in SPECIAL.items():
    args['arg'] = ts
    RESPONSE.append(args)

for path in FILES[:10]:
    if path not in SPECIAL:
        RESPONSE.append({
            'title': os.path.basename(path),
            'arg': path,
        })

print(json.dumps({'items': RESPONSE}))
