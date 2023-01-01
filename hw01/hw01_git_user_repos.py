import requests, json
from pprint import pprint

def get_repos():
    user = input("Enter user name: ")
    url = "https://api.github.com/users/{USER}/repos?per_page=1000"
    url = url.replace("{USER}", user)
    try:
        data = requests.get(url)
        data_json = data.json()
        repos = []
        for i in data_json:
            repos.append(i["name"])
    except:
        print("smth went wrong, try another user")
    return repos

print(get_repos())
