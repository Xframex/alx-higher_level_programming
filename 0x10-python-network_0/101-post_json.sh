#!/bin/bash
# Sends a Json POST
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
