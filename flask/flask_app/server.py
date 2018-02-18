#!/usr/bin/python3

from flask_api import FlaskAPI as flask
from configparser import ConfigParser
# Summarizing libraries
from mongo import fetch_data
from summary import send_request
from newspaper import Article
from flask import request
import thread
import json

# The THRESH variable is used to determine if a page has more than
# 100 words of text on it, which we believe equates to an article
THRESH = 100
app = flask(__name__)

@app.route("/summary/", methods=['GET', 'POST'])
def summary():
    # Gets URL from website
    search_request = str(request.args.get('website'))
    boom_request = str(request.query_string('boom'))

    if search_request:
        url = search_request
    else:
        url = boom_request

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
        try:
            # The first thread should return a JSON structure with a summary
            content = thread.start_new_thread(fetch_data, (url))
            # Calculates the acuracy of article
            calc = thread.start_new_thread(calculate, (text, authors, url))
            # 5 Seconds for threads to complete
            thread.join(5)
            # Joins to return to user in JSON structure
            content.valid.push({ value: calc })
            return content
        except:
            return "Error"
            # return fetch_data(url)
    # Return if page doesn't have an article
    else:
        return "Not Possible"

if __name__ == "__main__":
    app.run(debug=True)
