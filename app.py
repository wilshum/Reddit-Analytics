
from flask import Flask, render_template
from scrapReddit import scrap_func
from graphData import graph_func
from scrapReddit import top_submission
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.String(200), nullable=False)
    upvotes = db.Column(db.Integer, default = 0)

    def __repr__(self):
        return '<Submission %r>' % self.id
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/scrapReddit")
def scrapReddit():

    sname = 'wallstreetbets'
    scrap_func(sname)
    return "Scraping Reddit..."

@app.route("/graphData")
def graphData():
    graph_func()
    return "graph Data..."

@app.route("/topSubmissions")
def topSubmissions():

    sname = 'wallstreetbets'
    data = top_submission(sname)
    return data

if __name__ == '__main__':  #if python interpreter executes this
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)