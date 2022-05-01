#!/bin/env python3
import requests
import re

BASE_URL = "http://35.196.167.142:8082"
UUID_RE = re.compile(r'........-....-....-....-............')

res = requests.get(BASE_URL)
queue = set(UUID_RE.findall(res.text))
visited = set()

# BFS graph traversal
while len(queue) > 0:
    uuid = queue.pop()
    visited |= set([uuid])
    print(f"{uuid}...")

    res = requests.get(BASE_URL + "/article/" + uuid)
    matches = set(UUID_RE.findall(res.text))

    if len(matches) == 0:
        if "rip" in res.text:
            continue
        else:
            break
    else:
        queue |= (matches - visited)

print(res.text)