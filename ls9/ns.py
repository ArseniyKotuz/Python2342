import requests
from bs4 import BeautifulSoup
import re

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find(id="ResultsContainer")

job_elements = result.find_all("div", class_="card-content")

for job_element in job_elements:
    title = job_element.find("h2", class_='title')
    company = job_element.find("h3", class_='subtitle')
    location = job_element.find("p", class_="location")
    if re.findall(r'\bPython\b', title.text):
        formatted_location = location.text.replace(" ", "")
        print(f'{title.text} in {company.text} {formatted_location}')