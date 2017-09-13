#!/bin/sh
WORKLOG="$HOME/Documents/worklog/$(date -v+1d +'%Y-%m-%d-%Y%m%d.markdown')"
if [ ! -f "$WORKLOG" ]; then
sed "s|<date>|$(date -v+1d +'%Y-%m-%d')|g" template.markdown > "$WORKLOG"
fi
open "$WORKLOG"
