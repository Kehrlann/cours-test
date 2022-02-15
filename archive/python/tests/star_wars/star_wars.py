import requests


def list_movies():
    response = requests.get("https://swapi.co/api/films/").json()
    films = response['results']
    titles = [film['title'] for film in films]
    return sorted(titles)


if __name__ == "__main__":
    print(list_movies())
