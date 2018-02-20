#!/usr/bin/python3
# Author: Trvon, Tjwells

# Custom API's
from api.request_summary import request_function 
import api.oauth

# Imported Libaries
from flask_api import FlaskAPI as flask
from flask import request

# The THRESH variable is used to determine if a page has more than
# 100 words of text on it, which we believe equates to an article
# TODO: implement logging
# Log file read and write
# LOG.write(url)
# LOG = open("logs/python_log", "rw")
# LOG.close()

app = flask(__name__)

# This is where OAuth2 will be handled
# @app.route("/auth/", methods=[('GET', 'POST')]
# def authentication():
#    return "true"

@app.route("/summary/", methods=['GET', 'POST'])
def summary():
    # Gets URL from website
    url = str(request.args.get('website'))

    # Changing request back to standard request
    url = url.replace('%3A', ':')
    url = url.replace('%2F', '/')
    return request_function(url)
