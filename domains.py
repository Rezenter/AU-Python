__author__ = 'rezenter'
import urllib.parse
import urllib.request
import sys
import re
import collections

#word = urllib.parse.quote(sys.argv[1])
word = urllib.parse.quote("qwerty")
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('http://www.google.com/search?q=' + word, None, headers)
html = str(urllib.request.urlopen(req).read())
http = re.compile("<h3 class=\"r\"><a href=\"/url\?q=http://(?P<body>[^/]+)/")
list(http.finditer(html))
domains = []
for url in list(http.finditer(html)):
    domains.append(url.group("body"))
cut = re.compile("[a-z0-9а-я\.-]+\.(?P<dfl>[a-z0-9а-я]+)")
dfl = {}
for i in domains:
    tmp = cut.match(i).group("dfl")
    if tmp in dfl:
        dfl[tmp] += 1
    else:
        dfl[tmp] = 1


def sort_by(arg):
    return arg[1]
dfl = list(dfl.items())
dfl.sort(key=sort_by, reverse=True)
for i in dfl:
    print(i[0])