from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<button><a href="/static/singh.txt">click me</a></button>'