import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")
url = "https://www.reddit.com/r/{i}/top/?t=month"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/read")
def read():
    db = []
    headTitle = ""
    for i in subreddits:
        r = request.args.get(i)
        if r == "on":
            headTitle = headTitle + f"r/{i} "
            url = f"https://www.reddit.com/r/{i}/top/?t=month"
            html = requests.get(url, headers=headers)
            soup = BeautifulSoup(html.text, "html.parser")
            results = soup.find("div", "rpBJOHq2PR60pnwJlUyP0").find_all(
                "div", "_1oQyIsiPHYt6nx7VOmd1sz")
            for q in results:
                title = q.find("h3", "_eYtD2XCVieq6emjKBH3m").text
                upvote = q.find("div", "_1rZYMD_4xY3gRcSS3p8ODO").text
                link = q.find(
                    "div", "y8HYJ-y_lTUHkQIc1mdCq").find("a", "SQnoC3ObvgnGjWt90zD9Z")
                if link:
                    link = link["href"]
                    link = "https://www.reddit.com" + link
                    upvote = int(upvote.replace("k", "000").replace(".", ""))
                    things = {
                        "upvote": upvote,
                        "title": title,
                        "link": link,
                        "sort": "r/"+i
                    }
                    db.append(things)

    print(type(db))
    db = sorted(db, key=lambda x: x['upvote'], reverse=True)

    return render_template("read.html", db=db, headTitle=headTitle)


app.run(host="0.0.0.0")
