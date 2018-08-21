import requests
import beautifulscraper


url = "https://echo360.org.uk/lesson/8b41bed0-7022-4087-92ba-eef573dc4e29/classroom#sortDirection=desc"

res = requests.get(url)
print(res.text)