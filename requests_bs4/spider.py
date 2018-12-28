import requests

from bs4 import BeautifulSoup


journal_url = "http://www.rondonopolis.mt.gov.br/diario-oficial/"
response = requests.get(journal_url)

soup = BeautifulSoup(response.content, 'html.parser')
pdf_links = soup.find("table", {"class": "table-diary"}).find_all("a")

for link in pdf_links:
    print(link["href"])