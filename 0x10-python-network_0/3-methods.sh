#!/bin/bash
# Showing allowed methods
curl -sI "$1" | grep -i "Allow:" | awk '{for(i = 2; i <= NF; i++) printf (i == 2 ? "" : " ") $i}'
