#!/bin/bash
# Getting the body of the response (-X)=> for Method, (-L)=> for escaping the redirections and going for the final page
curl -sLX GET "$1"
