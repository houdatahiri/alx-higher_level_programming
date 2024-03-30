#!/bin/bash
# Bash script that takes in a URL and displays all HTTP 
curl -sI "$1" | grep -i allow | cut -d ' ' -f2-
