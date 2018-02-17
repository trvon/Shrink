from pymongo import MongoClient
from summary import send_request

client = MongoClient('localhost', 27017)
db = client['shrink_db']
summaries = db.summaries

def import_data(url):
    post_data = {
        'site': url,
        'summary': send_request(url)
    }
    result = summaries.insert_one(post_data)
    # print('One post: {0}].format(result.inserted_id))

def fetch_data(url):
    fetch = summaries.find_one({'site': url})
    if fetch:
        return fetch
    else:
        import_data(url)
        fetch_data(url)
