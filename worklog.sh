#!/bin/sh
WORKLOG="$HOME/Documents/worklog/$(date +'%Y-%m-%d-%Y%m%d.markdown')"
if [ ! -f "$WORKLOG" ]; then
cat > $WORKLOG <<EOF
---
layout: post
title: "Worklog $(date +'%Y-%m-%d')"
---
## Goals
*

## Log
*

## Later
*
EOF
fi
open "$WORKLOG"
