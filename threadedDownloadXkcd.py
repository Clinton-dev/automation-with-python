#! python 3.8.10

# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads

import requests
import bs4
import threading
import os

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download page
        print('Downloading the page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # find the url of comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Image not found!!')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:'+comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join(
                'xkcd', os.path.basename(comicUrl)), 'wb')

            for chunk in res.iter_content(100_000):
                imageFile.write(chunk)
            imageFile.close()


# Create and start thread objects
downloadThreads = []

for i in range(0, 140, 10):
    start = i
    end = i + 9

    if start == 0:
        start = 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for dowloadThread in downloadThreads:
    downloadThread.join()
print('Done')
