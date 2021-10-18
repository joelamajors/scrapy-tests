import scrapy
import json

with open("../../../urls.json", "r") as read_file:
    data = json.load(read_file)


class TagsCheckSpider(scrapy.Spider):
    name = "tags_check"
    start_urls = data["urls"]

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    def parse(self, response):
        tags = response\
                .xpath("//script[contains(@src, 'googletagmanager')]")\
                .getall()
        no_tags = "No tags found"

        url_tag_set = set()


        for tag in tags:
            url_tag_set.add
            {
                'url': ,
                'tag': tag if tag else no_tags
            }

        with open('tags.json', 'wb') as f:
            f.write(response.body)


"""
What do I want to do?
I want to get the response
print the url
print the response(s)
write that to a csv file

csv file
url,tag... more than one tag??

json file
url: string
code: 200,etc.
tag: set
"""
