import random
import ssl
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg")