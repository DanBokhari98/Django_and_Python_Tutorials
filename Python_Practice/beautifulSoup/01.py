from bs4 import BeautifulSoup
import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#print(page)


soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())


#list(soup.children)

[type(item) for item in list(soup.children)]


html = list(soup.children)[2]
#print(html)


soup = BeautifulSoup(page.content, 'html.parser')


print(soup.find_all('p')[0].get_text())
