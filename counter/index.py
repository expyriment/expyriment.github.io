#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

import urllib
import json


url = "https://pypi.python.org/pypi/Expyriment/json"
response = urllib.urlopen(url)
data = json.loads(response.read())
releases = data['releases'].keys()
releases.sort(reverse=True)
downloads = 0
for release in releases:
    if data['releases'][release] != []:
        for f in range(len(data['releases'][release])):
            downloads += data['releases'][release][f]['downloads'] 
        break


print "Content-Type: text/html"
print

print """
    <html>
    <head>
    <title>Expyriment Download Counter</title>
    <link rel='stylesheet' href='style.css'>
    <body>
    <div>
    <h1>Expyriment {0} downloads:</h1>
    <p>{1}</p>
    </div>
    </body>
    </html>
""".format(releases[0], downloads)
