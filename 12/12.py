from flask import Flask, render_template, request, redirect
from scrapper import aggregate_subreddits
import requests

app = Flask("RedditNews")

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


@app.route("/")
def home():
    return render_template("home.html", subreddits=subreddits)


@app.route("/add", methods=['POST'])
def add():
    url = "https://reddit.com/"
    r = request.form["new-subreddit"]
    resultUrl = url + r
    response = requests.get(resultUrl)
    code = response.status_code
    print(code)
    if "r/" in r:
        errorMassage = "Write the name without /r/"
    elif code <= 400:
        subreddits.append(r)
        return redirect("/")
    elif code == 429:
        errorMassage = "Too many Requests, Now. Please try again in a few minutes."
    else:
        errorMassage = "That subreddit does not exist."
    return render_template("add.html",
                           errorMassage=errorMassage)


@app.route("/read")
def read():
    selected = []
    for subreddit in subreddits:
        if subreddit in request.args:
            selected.append(subreddit)
    posts = aggregate_subreddits(selected)
    posts.sort(key=lambda post: post['votes'], reverse=True)
    return render_template("read.html", selected=selected, posts=posts)


app.run(host="0.0.0.0")
