#!/bin/bash
# Showing allowed methods
curl -sI "$1" | grep -i "Allow:" | awk
