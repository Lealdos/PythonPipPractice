""" this line

use to manipulate HTPP request
"""
import requests

API_URL_CATEGORIES = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(API_URL_CATEGORIES)
    print(f"HTPP response {r.status_code}")
    # print(r.text)
    categories = r.json()
    for category in categories:
        print(category['name'])
    