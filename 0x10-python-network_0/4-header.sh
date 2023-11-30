#!/bin/bash
#Bash script that sends a GET request, and displays the body response
curl -s "$1" -X GET -H "X-Hello School!-User-Id: 98"
