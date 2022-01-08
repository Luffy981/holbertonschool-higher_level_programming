#!/bin/bash
# cURL only methods
curl -sI "$1" | grep -i "allow:" | awk '{print $2}'
