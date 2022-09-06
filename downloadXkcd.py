#! python 3.8.13

# downloadXkcd.py - Downloads every single XKCD comic

import requests
import os
import bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # download the page
    print('Downloading page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # find the url of the image
    comicEle = soup.select('#comic img')
    if comicEle == []:
        print("couldn't find comic image.")
    else:
        comicUrl = 'https:' + comicEle[0].get('src')
        print('Downloading image %s ...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # svae the image to /xkcd
        imageFile = open(os.path.join(
            'xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the prev button urls
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')


print('Done!')
