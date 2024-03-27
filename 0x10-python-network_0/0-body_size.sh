#!/bin/bash
# printing a specific feild of the response of http (-I)=> for Getting HHTP-Header only
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
