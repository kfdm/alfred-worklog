#!/bin/sh
WORKLOG="$HOME/Documents/worklog/$(date +'%Y-%m-%d-%Y%m%d.markdown')"
if [ ! -f "$WORKLOG" ]; then
sed "s|<date>|$(date +'%Y-%m-%d')|g" template.markdown > "$WORKLOG"
fi
open "$WORKLOG"
