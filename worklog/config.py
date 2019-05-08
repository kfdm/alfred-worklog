import os


os.environ.setdefault("WORKLOG", os.path.join("~", "Documents", "worklog"))

WORKLOG_DIR = os.path.expanduser(os.environ["WORKLOG"])
WORKLOG_GLOB = os.path.join(WORKLOG_DIR, "*.markdown")
WORKLOG_FMT = "%Y-%m-%d.markdown"
