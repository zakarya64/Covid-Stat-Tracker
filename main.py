from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.nytimes.com/interactive/2021/world/covid-vaccinations-tracker.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
israel = page_soup.find("tr", {"class":"g-row-6 svelte-10f2uh3"})
israelreal = israel.find("td", {"class": "g-cell g-cell--vaccinated g-cell--fix g-cell--right g-cell--hide-mobile svelte-10f2uh3"})


print("the amount of people vaccinated in israel is " + israelreal.text)