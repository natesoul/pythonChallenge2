import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
newGroups = []
popGroups = []
app = Flask("DayNine")

newResult = requests.get(new).json()
for i in newResult['hits']:
    group = {}
    id = i['objectID']
    title = i['title']
    url = i['url']
    point = i['points']
    author = i['author']
    comment = i['num_comments']
    group = {
        "id": id,
        "title": title,
        "url": url,
        "point": point,
        "author": author,
        "comment": comment
    }
    newGroups.append(group)
db['new'] = newGroups

popularResult = requests.get(popular).json()
for i in popularResult['hits']:
    group = {}
    id = i['objectID']
    title = i['title']
    url = i['url']
    point = i['points']
    author = i['author']
    comment = i['num_comments']
    group = {
        "id": id,
        "title": title,
        "url": url,
        "point": point,
        "author": author,
        "comment": comment
    }
    popGroups.append(group)
db['popular'] = popGroups


@app.route("/")
def home():
    check = "popular"
    selectedGroup = db['popular']
    if request.args.get('order_by'):
        order = request.args.get('order_by')
        check = order
        if check == "popular":
            selectedGroup = db['popular']
        else:
            selectedGroup = db['new']
    return render_template("index.html", db=selectedGroup, check=check)


@app.route("/<int:id>")
def detail(id):
    groups = []
    detailUrl = make_detail_url(id)
    detailResult = requests.get(detailUrl).json()
    title = detailResult['title']
    point = detailResult['points']
    author = detailResult['author']
    url = detailResult['url']
    for i in detailResult['children']:
        group = {}
        commenter = i['author']
        text = i['text']
        group = {
            "author": commenter,
            "comment": text
        }
        groups.append(group)
    return render_template("detail.html", db=groups, title=title, point=point, url=url, author=author)


app.run(host="0.0.0.0")
