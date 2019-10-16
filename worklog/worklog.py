import collections
import datetime
import json

from worklog import config

RESPONSE = []
TODAY = datetime.datetime.today()
TOMORROW = TODAY + datetime.timedelta(days=1)
YESTERDAY = TODAY - datetime.timedelta(days=1)


SPECIAL = collections.OrderedDict()

SPECIAL[config.fromdt(TODAY)] = {"title": "Open Today for Editing"}

SPECIAL[config.fromdt(TOMORROW)] = {
    "title": "Open Tomorrow for Editing",
    "icon": {"path": "tomorrow.png"},
}

SPECIAL[config.fromdt(YESTERDAY)] = {
    "title": "Open Yesterday for Editing",
    "icon": {"path": "yesterday.png"},
}


def main():
    for ts, args in SPECIAL.items():
        args["arg"] = config.relative(ts)
        RESPONSE.append(args)

    for path in sorted(config.WORKLOG_GLOB, reverse=True)[:8]:
        if path not in SPECIAL:
            RESPONSE.append(
                {
                    "title": config.relative(path),
                    "arg": config.relative(path),
                    "icon": {"path": "review.png"},
                }
            )

    print(json.dumps({"items": RESPONSE}, cls=config.Encoder))
