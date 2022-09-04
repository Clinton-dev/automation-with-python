# ! python 3.9.13

"""
    Opens several search results
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

res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='
                   + ' '.join(sys.argv[1:]))
res.raise_for_status()

print(res)
