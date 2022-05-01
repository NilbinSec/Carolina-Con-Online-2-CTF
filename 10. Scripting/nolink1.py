#!/bin/env python3
import requests
import re

BASE_URL = "http://35.196.167.142:8081"
UUID_RE = re.compile(r'........-....-....-....-............')

res = requests.get(BASE_URL)
match = UUID_RE.search(res.text)

while match:
    uuid = match.group(0)
    print(uuid)
    res = requests.get(BASE_URL + "/article/" + uuid)
    match = UUID_RE.search(res.text)

print(res.text)