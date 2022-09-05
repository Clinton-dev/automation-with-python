#! python3.8.13

""" Opens top five search results from jumia """

import requests
import bs4
import webbrowser
import sys

print('searching products ....')
res = requests.get('https://www.jumia.co.ke/catalog/?q=' +
                   ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('.core')
noElems = min(5, len(elems))
for i in range(noElems):
    url = 'https://www.jumia.co.ke' + elems[i].get('href')
    print('Opening url to ...', url)
    webbrowser.open(url)
