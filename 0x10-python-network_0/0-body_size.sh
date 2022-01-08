#!/usr/bin/env bash
# cURL body size
URL_IP="$1"
curl -sI "$URL_IP" | grep -i Content-Length | awk 'print $2'
