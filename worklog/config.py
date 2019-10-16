import os
import pathlib
import datetime
from json import JSONEncoder

os.environ.setdefault("WORKLOG", os.path.join("~", "Documents", "worklog"))

WORKLOG_DIR = pathlib.Path(os.environ["WORKLOG"]).expanduser().resolve()
WORKLOG_GLOB = WORKLOG_DIR.glob("**/**/*.markdown")


class Encoder(JSONEncoder):
    def default(self, o):
        return str(o)


def fromdt(dt: datetime.datetime):
    return (
        WORKLOG_DIR
        / str(dt.year)
        / str(dt.month)
        / f"{dt.year}-{dt.month}-{dt.day}.markdown"
    )


def relative(path: pathlib.Path):
    return path.relative_to(WORKLOG_DIR)
