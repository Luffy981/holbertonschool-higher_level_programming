#!/bin/bash
# status code
curl -so /dev/null -sw '%{http_code}\n' "$1"
