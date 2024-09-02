import ctypes
import os
import requests
import tempfile


def getImageUrl():
    jsonUrl = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-us'
    r = requests.get(jsonUrl)
    json = r.json()
    url = json['images'][0]['url']
    url = url.split('&')[0]
    url = 'https://www.bing.com' + url
    return url


def setWallpaper(url):
    r = requests.get(url)
    fname = url.split('=OHR.')[1]
    furl = os.path.join(tempfile.gettempdir(), fname)
    open(furl, 'wb').write(r.content)
    os.path.isfile(furl)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(furl), 3)
    os.remove(furl)


if __name__ == '__main__':
    url = getImageUrl()
    setWallpaper(url)
