#!/usr/bin/python3

from flask_api import FlaskAPI as flask
from configparser import ConfigParser
# Summarizing libraries
from mongo import fetch_data
from summary import send_request
from newspaper import Article
from flask import request
import json

# The THRESH variable is used to determine if a page has more than
# 100 words of text on it, which we believe equates to an article
THRESH = 100
app = flask(__name__)

@app.route("/summary/", methods=['GET', 'POST'])
def summary():
    # Gets URL from website
    url = str(request.args.get('website'))
    
    # Changing request back to standard request
    url = url.replace('%3A', ':')
    url = url.replace('%2F', '/')
   
    # Preparing URL for analysis
    a = Article(url)
    
    a.download()
    a.parse()
    authors = a.authors
    
    # Checking if the webpage contains authors
    if authors:
        return fetch_data(url)
   
    # Return if page doesn't have an article
    else:
        return url

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
