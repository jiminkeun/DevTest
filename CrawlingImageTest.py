import urllib.request as req
from bs4 import BeautifulSoup

# 이미지 다운로드
def download_img(furl):
    savePath = "E:/Data/크롤링자료/9seke.com/"
    imgName = furl.replace("http://p9.x1994.com/I/","")
    print(furl + "~~" + (savePath+imgName))
    #req.urlretrieve(furl,savePath+imgName)

hdr = {'User-Agent':'Mozilla/5.0','referer':'http://www.9seke.com'}
url = "http://www.9seke.com/article/html/11396.html"
enc_url = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = req.urlopen(enc_url)
source = html.read().decode('utf-8')
html.close()

soup = BeautifulSoup(source, "html5lib")
img_source = soup.find("div", {"class":"content"}).find_all("img")

#print(img_source)


for img_item in img_source:
    download_img(img_item.get("src"))
    url = img_item.get("src")
    #urlopen.urlretrieve(url, url.replace("http://p9.x1994.com/I/",""))
    print(url + " 다운로드 완료 \n")


