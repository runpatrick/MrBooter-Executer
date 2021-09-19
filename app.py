import flask
from flask import request
from flask import Flask, render_template
import time
app = flask.Flask(__name__)

@app.route("/")
def index():
  host = request.args.get('host')
  length = request.args.get('length')
  if host == None:
    return("Please fill out the required!");
  else:
    return(host);
  if length == None:
    return("Please fill out the required!");
  else:
    return(length);
    test();
  return "{Executer: Online}"

def test():
  return "It worked!"

