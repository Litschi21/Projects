import requests
from bs4 import BeautifulSoup

try:
    r = requests.get('https://news.google.com/home?hl=en-US&gl=US&ceid=US:en', timeout=5)
except requests.exceptions.Timeout:
    print('Request timed out.')
    quit()

soup = BeautifulSoup(r.text, 'html.parser')

def filter(tag):
    filter_words = ['Consumer Information', 'News', 'Sign in', 'Home', 'For you', 'Following', 'News Showcase', 'U.S.', 'World', 'Local', 'Business', 'Technology', 'Entertainment', 'Sports', 'Science', 'Health', 'Learn more', 'Google Weather', 'Top stories']
    lines = []
    
    for line in soup.find_all(tag):
        if not line in filter_words:
            lines.append(line)
    
    return lines

for title in soup.find_all(filter('a')):
    print(title.get_text())
