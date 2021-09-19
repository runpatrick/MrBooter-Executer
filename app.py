import flask
from flask import request
app = flask.Flask(__name__)

@app.route("/")
def index():
  host = request.args.get('host')
  length = request.args.get('length')
  if host == None:
    print("Please fill out the required!");
  else:
    print(host);
  if length == None:
    print("Please fill out the required!");
  else:
    print(length);
  return render_template("index.html")
