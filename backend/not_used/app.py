import datetime
import os
from pathlib import Path
import json
import pandas as pd


 
from flask import Flask, Response, request
#from flask_mongoengine import MongoEngine

app = Flask(__name__)
#app.config['MONGODB_SETTINGS'] = {
#    'host': os.environ['MONGODB_HOST'],
#    'username': os.environ['MONGODB_USERNAME'],
#    'password': os.environ['MONGODB_PASSWORD'],
#    'db': 'webapp'
#}
#db = MongoEngine()
#db.init_app(app)
#
#class Todo(db.Document):
#    title = db.StringField(max_length=60)
#    text = db.StringField()
#    done = db.BooleanField(default=False)
#    pub_date = db.DateTimeField(default=datetime.datetime.now)

@app.route("/api")
def index():
    Todo.objects().delete()
    Todo(title="Simple todo A", text="12345678910").save()
    Todo(title="Simple todo B", text="12345678910").save()
    Todo.objects(title__contains="B").update(set__text="Hello world")
    todos = Todo.objects().to_json()
    return (Response(todos, mimetype="application/json", status=200))

@app.route("/")
def hello_world():
    return ("<p>Hello, World!</p>")

@app.route("/components")
def serve_components():
    component_paths = [str(j)  for i in list((Path.cwd().parent / "components").iterdir()) for j in list(i.iterdir())]
    component_jsons = [pd.read_json(i, orient='index').to_dict() for i in component_paths if Path(i).suffix == ".json"]
    component_svg = [Path(i).read_text() for i in component_paths if Path(i).suffix == ".svg"]
    return(component_jsons[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)