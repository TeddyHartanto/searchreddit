#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


# crawling
def download_page(url):
    resp = requests.get(url)
    while resp.status_code != 200:
        resp = requests.get(url)
    return resp.text

def parse_html(url, html):
    path = urlparse(url).path.split('/')
    uid = path[-3]
    soup = BeautifulSoup(html, 'html.parser')
    selected = soup.select('div#thing_t3_{0} div.md'.format(uid))[0]
    return selected.get_text()

if __name__ == '__main__':
    url = sys.argv[1]
    html = download_page(url)
    content = parse_html(url, html)
    print(content)
    
