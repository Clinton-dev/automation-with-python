#! python 3.9.13

"""
    Opens several search results in pypi.org
"""
import requests
import sys
import webbrowser
import bs4
# Todos:
# Read the command line args
# fetch the search result page
# find links to each search result
#  open the web browser

print('Searching ....')

res = requests.get('https://pypi.org/search/?q='
                   + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    # TODO: Open a browser tab for each result.
    print('Opening... ', urlToOpen)
    webbrowser.open(urlToOpen)
