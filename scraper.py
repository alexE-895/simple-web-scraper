import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []

for h1 in soup.find_all("h1"):
    titles.append(h1.text.strip())

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title"])

    for t in titles:
        writer.writerow([t])

print("Scraping finished")
