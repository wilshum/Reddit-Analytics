
from flask import Flask
app = Flask(__name__)

# import scrapReddit
# import graphData


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/scrapReddit")
def scrapReddit():
    import scrapReddit
    return "Scraping Reddit..."


@app.route("/graphData")
def graphData():
    import graphData
    return "graph Data..."

