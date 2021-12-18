import bs4
import requests

base_url = 'https://quotes.toscrape.com/page/{}/'
authors_list = []
i = 1

while True:

    scrape_url = base_url.format(i)
    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    authors = soup.select(".author")

    if len(authors) == 0:
        break

    for author in authors:

        if author.text not in authors_list:
            authors_list.append(author.text)

    i = i + 1

print(authors_list)