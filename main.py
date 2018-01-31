#pip install requests && pip install BeautifulSoup
from bs4 import BeautifulSoup
import requests
import shutil
import random


def getBandname(url):
    url = url
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    firstH2 = soup.find('h2') # Start here
    uls = []
    for nextSibling in firstH2.findNextSiblings():
        #print(nextSibling)
        #print(nextSibling.name)
        if nextSibling.name == 'ul':
            uls.append(nextSibling)
    #print (uls)
    lis = []
    #print(lis)
    for ul in uls:
        for li in ul.findAll("li"):
            #print(li)
            lis.append(li)
    if not lis:
        getBandname(url)
    else:
        print("Band:")
        bandname = lis[-1].text.encode("utf-8")
        print (bandname)
    
def getAlbumname(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    albumname = soup.find('b') # Start here
    print("Album:")
    print(albumname)

def getAlbumpicture(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    #print(soup)
    td = soup.find_all("td", class_="Photo") # Start here
    print("AlbumART:")
    pix = []
    for img in td:
        for links in img.find_all('a'):
            pix.append("https://www.flickr.com"+links.get('href'))
    picurl = random.choice(pix)
    #print(picurl)
    r  = requests.get(picurl)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    picture = soup.find("meta",  property="og:image")
    albumart = picture.get('content')
    print(albumart)

  
    #filename = url.split("/")[-1]
    #r = requests.get(url, timeout=0.5)
    #if r.status_code == 200:
    #    with open(filename, 'wb') as f:
    #        f.write(r.content)

if __name__ == '__main__':
    getBandname("https://en.wikiquote.org/wiki/Special:Random");
    getAlbumname("https://en.wikipedia.org/wiki/Special:Random");
    getAlbumpicture("https://www.flickr.com/explore/interesting/7days/");

