# create a web scraper that will scrape the website https://realpython.github.io/fake-jobs/

import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)


