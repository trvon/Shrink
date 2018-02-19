#!/usr/bin/python
from urllib3.util.url import parse_url
import language_check as LChecker
# import dblp

def author_check(authors):
    publications = 0
    for author in authors:
        publications = author_lookup(author) + publications
    return publications

# Need to locate dblp for python3
# TODO: Fix this functoin
# def author_lookup(author):
#    author = dblp.search(author)
#    return len(michael.publications)

def language_check(text):
    tool = LChecker.LanguageTool('en-US')
    errors = tool.check(text)
    # We need to determine how many errors is to many
    num = len(errors)
    if num > 100:
        num = num % 100
    return num

# Interesting guide for urllib3
# https://gist.github.com/JordanMilne/17e413fafb3673f9b64a
def url_check(url):
    # The weight of these values isn't to high so the value of a given 
    # extension is subject to change
    value = {'org': 5.0, 'com': 3.0, 'edu': 5.0, 'gov': 5.0, 'net': 4.0, 'me': 2.0}    
    result = parse_url(url.rsplit('//',1)[1]).host.split('.')[-1]
    return value[result]

# Will need to implement something more robust
# https://martin-thoma.com/python-check-wiki-references-for-citation-template/
def citation_check(text):
    i = 0

def calculate(text, authors, url):
    percentage = float(((url_check(url) / 5)))  # + (100 - language_check(text))) / 2)
    return percentage
