#!/usr/bin/python
from nlp.summarizer import summarize
from pymongo import MongoClient
from urllib3.util.url import parse_url
import json

def mongo_start(url, text):
    host = parse_url(url).host.split('.')[1]
    client = MongoClient('127.0.0.1', 27017)
    db = client['shrink_db'] 
    summaries = db.host
    return fetch_data(url, summaries, text)

def import_data(url, summaries, text):
    if len(text) > 1000:
        post = summarize(text, None, 9)
    elif len(text) > 750:
        post = summarize(text, None, 7)
    else:
        post = summarize(text)
    # post = send_request(url)
    post_data = {
        'site': url,
        'summary': post
    }
    result = summaries.insert_one(post_data)
    return post

def fetch_data(url, summaries, text):
    fetch = summaries.find_one({'site': url})
    if not fetch: 
        return import_data(url, summaries, text)
    else:
        return fetch['summary']

