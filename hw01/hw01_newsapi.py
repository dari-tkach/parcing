"""
newsapi.org: Собрать новости, содердащие в заголовке Python, с 01/01/2023, записать в файл json.
"""


import requests, json
from pprint import pprint


def write_json(d: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(d, f, indent=2)


# GET https://newsapi.org/v2/everything?q=Apple&from=2023-01-01&sortBy=popularity&apiKey=API_KEY

url = ('https://newsapi.org/v2/everything?'
       'q=Python&'
       'searchIn=title&'
       'language=en&'
       'from=2023-01-01&'
       'sortBy=popularity&'
       'apiKey=09dd9d471b0746adac2098777b4ff1e2')

response = requests.get(url).json()
filename = "news_python.json"
write_json(response, filename)
# pprint(response)
