#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL
curl -H "X-School-User-Id: 98" -s "$1"
