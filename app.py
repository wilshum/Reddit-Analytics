
from flask import Flask, render_template
from scrapReddit import scrap_func
from graphData import graph_func
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/scrapReddit")
def scrapReddit():
    scrap_func()
    return "Scraping Reddit..."

@app.route("/graphData")
def graphData():
    graph_func()
    return "graph Data..."

if __name__ == '__main__':  #if python interpreter executes this
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)