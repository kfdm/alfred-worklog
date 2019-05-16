import collections
import datetime
import json

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


def main():
    for ts, args in SPECIAL.items():
        args['arg'] = ts
        RESPONSE.append(args)

    for path in sorted(config.WORKLOG_GLOB, reverse=True)[:8]:
        if path not in SPECIAL:
            RESPONSE.append(
                {"title": path.name, "arg": path.name, "icon": {"path": "review.png"}}
            )

    print(json.dumps({"items": RESPONSE}))
