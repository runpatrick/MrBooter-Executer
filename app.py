from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from flask import Flask, render_template
from flask import request
import time
import os
app = Flask(__name__)


@app.route('/')
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
    execute();
  #return render_template("index.html")
def execute():
  options = Options()
  options.binary_location = GOOGLE_CHROME_BIN
  options.add_argument('--disable-gpu')
  options.add_argument('--no-sandbox')
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--headless")
  ua = UserAgent()
  userAgent = ua.random
  print(userAgent)
  options.add_argument(f'user-agent={userAgent}')
  driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)
  driver.get("https://katacoda.com/embed/runpatrick/courses/challenges/node-challenge-1/?v=2&embed=true&ui=inline&host=137.184.30.68&url=http%3A%2F%2F137.184.30.68%2Ftest%2F%3Fhost%3D1&target=katacoda-scenario-1&nonce=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWJlZCI6dHJ1ZSwiZG9tYWluIjoiaHR0cDovLzEzNy4xODQuMzAuNjgvIiwiaXAiOiIyNC4yMjguMTA5LjI1NSIsImlhdCI6MTYzMTg2NTgzMiwiZXhwIjoxNjMxODY1ODYyfQ.DA-Sa33cRPy1IrloJNxqvIs37wotHl6KdSgyzCNYNPg&color=004d7f")
  time.sleep(7)
  #driver.save_screenshot("katacoda.png")
  url = driver.execute_script("return document.getElementById('weburl').innerText;")
  print(url)
