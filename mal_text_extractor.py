import requests

user = input()

url = "https://api.jikan.moe/v3/user/{}/animelist/completed".format(user)

response = requests.get(url)

json = response.json()

animelist = json["anime"]

for anime in animelist:
    print(anime["title"])
