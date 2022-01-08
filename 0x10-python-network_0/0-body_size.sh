#!/usr/bin/env bash
# cURL body size
URL_IP="$1"
curl "$URL_IP" -w '%{size_request}' -so /dev/null
echo
