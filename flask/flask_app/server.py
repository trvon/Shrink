#!/usr/bin/python3
# Author: Trvon, Tjwells

from flask_api import FlaskAPI as flask
from configparser import ConfigParser
# Summarizing libraries
from urllib3.util.url import parse_url
from mongo import fetch_data
from summary import send_request
from newspaper import Article
from flask import request
# import threading
from cred import calculate
import newspaper
import demjson
import json

# The THRESH variable is used to determine if a page has more than
# 100 words of text on it, which we believe equates to an article
THRESH = 150
# LOG = open("logs/python_log", "rw")
app = flask(__name__)

@app.route("/summary/", methods=['GET', 'POST'])
def summary():
    # Gets URL from website
    boom_request = str(request.args.get('website'))
    url = boom_request

    # Changing request back to standard request
    url = url.replace('%3A', ':')
    url = url.replace('%2F', '/')
    result = parse_url(url).path.split('/')
    
    # TODO: implement loggin

    # Log file read and write
    # LOG.write(url)
    # LOG.close()
    
    # Preparing URL for analysis
    a = Article(url)
    a.download()
    # Added check to see if the website is parsible by the API
    
    # TODO: Implement our our webscraper that parses the contents of websites
    try:
        a.parse()
    except ArticleException():
        return "Not Possible"

    authors = a.authors
    text = a.text 
   

    # Check if the webste is a homepage or not
    if len(result) > 2:
        # Passes url to the NLP API
        content = fetch_data(url)
        # Determines whether the process was possible or not
        if content is None:
            return "Not Possible"
        else:
            content = json.loads(content)
        # TODO: Finish computation of credibility
        # Logic of appending credibility to structure returned to the chrome extension
        calc = calculate(text, authors, url)
        content['value'] = calc
        content = json.dumps(content)
        return content
    
        # try:
        #    # The first thread should return a JSON structure with a summary
        #    content = thread.start_new_thread(fetch_data, (url))
        #    # Calculates the acuracy of article
        #    calc = thread.start_new_thread(calculate, (text, authors, url))
        #    # 5 Seconds for threads to complete
        #    thread.join(5)
        #    #Joins to return to user in JSON structure
        #    content.valid.push({ value: calc })
        #    return content
        # except:
        #    return "Error"
        #     return fetch_data(url)
        # Return if page doesn't have an article
    else:
        return "Not Possible"

if __name__ == "__main__":
     app.run(debug=True)
