import requests
import xmltodict
import json


# Remark: you could use feedparser, but this is more fun:
url = "https://www.oeamtc.at/feeds/verkehr/vorarlberg"

r = requests.get(url)
text = r.text
dict = xmltodict.parse(text)
json_data = json.loads(json.dumps(dict))

for i in json_data["rss"]["channel"]["item"]:
    print(i["guid"]["#text"])
    print(i["title"])
    print(i["link"])
    print(i["category"])
    print(i["description"])
    print(i["pubDate"])
    print("- " * 20)
    print()


# rss
#   channel
#     title
#     link
#     atom:link
#     description
#     language
#     copyright
#     pubDate
#     lastBuildDate
#     docs
#     ttl
#     image
#       title
#       url
#       link
#     item
#        guid
#        title
#        link
#        category
#        description
#        pubDate
#        georss:point
