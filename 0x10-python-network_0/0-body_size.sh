#!/usr/bin/bash
# printing a specific feild of the response of http
curl -sI "$1" | grep Content-Length | awk '{print $2}'
