import requests
import sys

def main(argv):
    user = argv[0]

    url = "https://api.jikan.moe/v3/user/{}/animelist/completed".format(user)

    response = requests.get(url)

    json = response.json()

    animelist = json["anime"]

    for anime in animelist:
        print(anime["title"])

if __name__ == "__main__":
    main(sys.argv[1:])
