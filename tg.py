from bs4 import BeautifulSoup
import requests

def telegram(username):
    baseurl = f"https://telegram.dog/{username}"
    r = requests.get(baseurl)
    soup = BeautifulSoup(r.text, "lxml")
    cname = soup.find("div", {"class": "tgme_page_title"}).find("span").text
    csubs = soup.find("div", {"class": "tgme_page_extra"}).text
    cdes = soup.find("div", {"class": "tgme_page_description"}).text
    cimg = soup.find("img", {"class": "tgme_page_photo_image"}).attrs["src"]

    #print(cname, csubs, cdes)
    data = {}
    data['name']= cname
    data['subs']= csubs
    data['des']= cdes
    data['image'] = cimg
    return data
    

#telegram("gdriveflixbd")