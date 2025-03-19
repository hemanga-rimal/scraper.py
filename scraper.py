# create a web scraper that will scrape the website https://realpython.github.io/fake-jobs/

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(page.text)


