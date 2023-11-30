#!/bin/bash
# script that takes displays the size of the body response of an url
curl -sI "$1" | grep 'Content-Length:' | cut -d " " -f 2
