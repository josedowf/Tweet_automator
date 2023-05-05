import logging
import requests
from bs4 import BeautifulSoup

google_search = 'DeFi news today'

# make two strings with default google search URL
# 'https://google.com/search?q=' and our customized search keyword and concatenate them
url = 'https://google.com/search?q=' + google_search + '&rlz=1C5CHFA_enMX868MX868&sxsrf=ALiCzsZ-jCmLfts0QLqa' \
                                                       '_csJ6C3WUZ30IA:1668705724126&source=lnms&tbm=nws&sa=' \
                                                       'X&ved=2ahUKEwiT966f3bX7AhUGATQIHbinDXsQ_AUoAXoECAEQAw' \
                                                       '&biw=800&bih=834&dpr=2'

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
# uncomment the print func below to see the page sources' HTML
# print(soup.prettify())

# Creating soup from the fetched request
soup = BeautifulSoup(html_content, "html5lib")
for item in soup.find_all('div', attrs={'class': 'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
    # finds title using the class that captured the title text within the html code
    # and replaces commas within the text in order to save it into a csv file with no conflict (comma
    # separated document). This process is repeated for the other elements as well.
    title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
    title = title.replace(",", "")

    author = item.find('div', attrs={'class': 'BNeawe UPmit AP7Wnd lRVwie'}).get_text()

    # splits the retrieved url and splits it, so it only takes the correct url.
    raw_link = (item.find('a', href=True)['href'])
    link = (raw_link.split('/url?q=')[1]).split('&sa=U&')[0]

    description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())
    description = description.replace(",", "")
    descript = description.split(' ... ')[0]

    raw_time = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}))
    time = raw_time.find('span', attrs={'class': 'r0bn4c rQMQod'}).get_text()

    print(title)
    print(author)
    print(link)
    print(descript)
    print(time)