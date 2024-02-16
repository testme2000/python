
from urllib.request import urlopen

print("Python : Web Scrapper")
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_info = page.read()
html_string = html_info.decode('utf-8')
print(html_string)