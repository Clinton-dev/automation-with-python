#! python 3.8.10

# downloadWallpaper.py - Downloads wallpapers and saves it to download-wallpapers

# Go to homepage http://wallpaperswide.com/
# Download the homepage using bs4
# get list of img
# loop over and get href link to individual page
# download the page and get the image url base on ur laptops screen size
import bs4
import requests
import os
import threading

url = 'http://wallpaperswide.com'
os.makedirs('wallpaperswide', exist_ok=True)

print('Downloading home page %s ...' % url)


def get_individual_pic_urls(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    pictureThumbNails = soup.find_all('div', class_='thumb')
    individualPictureUrl = [url + picture.a['href']
                            for picture in pictureThumbNails]
    return individualPictureUrl


# for imageUrl in imageUrls:
imageUrls = get_individual_pic_urls(url)


def downloadWallpaper(url):
    # download individual pic html page
    print('Downloading Page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    imageSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    imageLink = imageSoup.find('a', text='1366x768')['href']
    # download image
    link = 'http://wallpaperswide.com' + imageLink
    print('Downloading image %s ...' % link)
    resImg = requests.get(link)
    resImg.raise_for_status()
    # save image to /wallpaperswide

    imgFile = open(os.path.join('wallpaperswide',
                   os.path.basename(link)), 'wb')

    for chunck in resImg.iter_content(100_000):
        imgFile.write(chunck)
    imgFile.close()


downloadThreads = []
for i in imageUrls:
    downloadThread = threading.Thread(
        target=downloadWallpaper, args=(i,))
    downloadThreads.append(downloadThread)
    downloadThread.start()


# Wait for all threads
for downloadThread in downloadThreads:
    downloadThread.join()

# for i in imageUrls:
#     downloadWallpaper(i)

print('Done')
