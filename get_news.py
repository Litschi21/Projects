import requests
from bs4 import BeautifulSoup

try:
    r = requests.get('https://news.google.com/home?hl=en-US&gl=US&ceid=US:en', timeout=5)
except requests.exceptions.Timeout:
    print('Request timed out.')
    quit()

soup = BeautifulSoup(r.text, 'html.parser')

for title in soup.find_all('a'):
    print(title.get_text())
