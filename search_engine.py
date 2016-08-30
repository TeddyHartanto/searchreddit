#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

url = sys.argv[1]

# crawling
resp = requests.get(url)
while resp.status_code != 200:
    resp = requests.get(url)

path = urlparse(url).path.split('/')
uid = path[-3]

# parsing
soup = BeautifulSoup(resp.text, 'html.parser')
selected = soup.select('div#thing_t3_{0} div.md'.format(uid))[0]
print(selected.get_text())
