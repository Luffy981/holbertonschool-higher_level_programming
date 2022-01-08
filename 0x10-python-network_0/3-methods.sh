#!/bin/bash
# cURL only methods
curl -sI OPTIONS  https://www.sercoplus.com/ | grep -i "allow" | cut -d ':' -f2
