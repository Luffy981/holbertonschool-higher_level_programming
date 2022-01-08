#!/bin/bash
# cURL only methods
curl -sI "$1" | grep -i "allow" | cut -d ':' -f2
