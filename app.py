from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from flask import Flask, render_template
from flask import request
import requests
from requests.structures import CaseInsensitiveDict
import time
import os

app = Flask(__name__)


@app.route('/')
def index():
  host = request.args.get('host')
  length = request.args.get('length')
  method = request.args.get('method')
  if host == None:
    print("Please fill out the required!");
  else:
    print(host);
    prehost = host;
  if method == None:
    print("Please fill out the required!");
  else:
    print(method);
    premethod = method;
  if length == None:
    print("Please fill out the required!");
  else:
    print(length)
    prelength = length;
    execute();
  return '{Executer: Online}'


def execute():
    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
    host = request.args.get('host')
    length = request.args.get('length')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome('/Users/patrickschmidt/Desktop/chromedriver',chrome_options=options)
    driver.get("https://trinket.io/python3/980ef28a2b")
    driver.execute_script('document.getElementById("trinket-iframe").contentWindow.document.getElementsByClassName("jqconsole-prompt-text")[0].innerText="'+host+'"')
    actions = ActionChains(driver)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    time.sleep(int(length))
    driver.quit();

