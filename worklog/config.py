import os
import pathlib


os.environ.setdefault("WORKLOG", os.path.join("~", "Documents", "worklog"))

WORKLOG_DIR = pathlib.Path(os.environ["WORKLOG"]).expanduser().resolve()
WORKLOG_GLOB = WORKLOG_DIR.glob("*.markdown")
WORKLOG_FMT = "%Y-%m-%d.markdown"
