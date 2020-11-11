import requests
import xmltodict
import json


# ------------------------------------------------------------------------------
# Request RSS traffic ÖAMTC
# ------------------------------------------------------------------------------


# Remark: Maybe the package "feedparser" is a helpful option here

# German link is for Vorarlberg, English is only available for Austria (?)
# It is difficult to map the items for German and English because they have
# no similarities (Even headlines, time and coordinates differ)
url_de = "https://www.oeamtc.at/feeds/verkehr/vorarlberg"
#url_en = "https://www.oeamtc.at/verkehrsservice/output/rss/oeamtc_traffic_informations_austria.xml"

r = requests.get(url_de)
status = r.status_code

if status == 200:
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
else:
    print("Error {}".format(status))


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
