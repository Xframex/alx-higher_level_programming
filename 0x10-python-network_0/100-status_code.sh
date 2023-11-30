#!/bin/bash
#Displays status code of the response.
curl -sLw "%{http_code}" "$1" -o /dev/null
