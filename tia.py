import requests
import pandas as pd
import re
from time import sleep
from datetime import datetime

base_url = 'https://www.techinasia.com/wp-json/techinasia/2.0/posts?'
auto_url = 'https://www.techinasia.com/wp-json/techinasia/2.0/posts?page=1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
params = 'page='

def clean_tags(text):
    '''
    Clean html tags in content.
    ---------------------------
    Parameter:
    text(str): input text containing html.
    ---------------------------
    Return:
    clean_text
    '''
    pattern = re.compile('<.*?>')
    clean_text = re.sub(pattern, '', text).replace('\n', '').replace('\xa0', '')
    return clean_text

def get_data(url, params, headers):
    '''
    Get data from API
    ---------------------------
    Parameters:
    url(str): input url to get data.
    params(str): page parameter for pagination.
    headers(*args): headers to avoid 418 teapot.
    ---------------------------
    Return:
    pandas DataFrame
    '''
    all_data = []

    for page in range(1, 31):
        print(f"Page: {page}/30", end='\r')
        req = requests.get(url=url + params + str(page), headers=headers)
        json = req.json()

        for idx, post in enumerate(json['posts']):
            data = {
                'id': post['id'],
                'date_gmt': post['date_gmt'],
                'modified_gmt': post['modified_gmt'],
                'title': post['title'],
                'slug': post['slug'],
                'status': post['status'],
                'type': post['type'],
                'link': post['link'],
                'content': clean_tags(json['posts'][idx]['content']),
                'vsitems': post['vsitems'],
                'live_items': post['live_items'],
                'excerpt': post['excerpt'],
                'author_id': post['author']['id'],
                'author_name': post['author']['display_name'],
                'author_is_staff': post['author']['is_staff'],
                'editor': post['editor'].replace('Editing by ', ''),
                'comment_status': post['comment_status'],
                'comments_count': post['comments_count'],
                'comments': post['comments'],
                'categories': [cat['name'] for cat in json['posts'][idx]['categories']],
                'tags': [tag['name'] for tag in json['posts'][idx]['tags']],
                'companies': post['companies'],
                'is_sponsored': post['is_sponsored'],
                'sponsor_name': post['sponsor']['name'],
                'is_partnership': post['is_partnership'],
                'show_ads': post['show_ads'],
                'is_subscriber_exclusive': post['is_subscriber_exclusive'],
                'is_paywalled': post['is_paywalled'],
                'is_inappbrowser': post['is_inappbrowser'],
                'read_time': post['read_time']
            }
            all_data.append(data)
        sleep(3)        
    return pd.DataFrame(all_data)

def auto_get(url, params, headers):
    '''
    Get data from API automatically
    ---------------------------
    Parameters:
    url(str): input url to get data.
    params(str): page parameter for pagination.
    headers(*args): headers to avoid 418 teapot.
    ---------------------------
    Return:
    pandas DataFrame
    '''
    all_data = []

    req = requests.get(url=auto_url + params, headers=headers)
    json = req.json()

    for idx, post in enumerate(json['posts']):
        data = {
            'id': post['id'],
            'date_gmt': post['date_gmt'],
            'title': post['title'],
            'slug': post['slug'],
            'type': post['type'],
            'content': clean_tags(json['posts'][idx]['content']),
            'excerpt': post['excerpt'],
            'author_id': post['author']['id'],
            'author_name': post['author']['display_name'],
            'author_is_staff': post['author']['is_staff'],
            'editor': post['editor'].replace('Editing by ', ''),
            'comments_count': post['comments_count'],
            'categories': [cat['name'] for cat in json['posts'][idx]['categories']],
            'tags': [tag['name'] for tag in json['posts'][idx]['tags']],
            'is_sponsored': post['is_sponsored'],
            'sponsor_name': post['sponsor']['name'],
            'show_ads': post['show_ads'],
            'is_subscriber_exclusive': post['is_subscriber_exclusive'],
            'is_paywalled': post['is_paywalled'],
            'is_inappbrowser': post['is_inappbrowser'],
            'read_time': post['read_time']
        }
        all_data.append(data)      
    return pd.DataFrame(all_data)