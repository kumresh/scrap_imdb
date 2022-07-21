import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/search/title/?genres=action,fantasy,sci-fi&companies=universal"
count = 0


def getIMDBdata():
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    movie_div = soup.find("div", class_="lister-list")

    for i in movie_div.find_all("div", class_="lister-item mode-advanced"):
        img_list = i.find("img")
        movieTitle = img_list.get("alt")
        movieImg = img_list.get("loadlate")

        print(movieTitle, " = ", movieImg)
        if count == 8:
            break
        count += 1


def main():
    getIMDBdata()
