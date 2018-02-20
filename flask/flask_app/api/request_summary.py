#Library imports
from urllib3.util.url import parse_url
from newspaper import Article
# Custom imports
from api.mongo import fetch_data
from api.cred import calculate
import json

def request_function(url):
    result = parse_url(url).path.split('/')
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
    else:
        return "Not Possible"
