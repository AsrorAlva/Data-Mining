import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.halodoc.com/')
soup = BeautifulSoup(page.content, 'html.parser')
print(page.status_code)