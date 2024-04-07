import bs4
import requests
import os
import sys

def get_response(link):
    response = requests.get(link)
    if response.status_code != 200:
        exit(1)
    else:
        response.encoding = "utf-8"
        page = response.text
        return page

def chapter_links_asura(page):
    text = bs4.BeautifulSoup(page, 'html.parser')

    chapters = text.find(id="chapterlist").find(class_="clstyle")
    li = chapters.find_all("li")
    chapter_links = []
    links=[]
    
    for i in li:
        link = i.find("div", class_="chbox").find("div", class_="eph-num").find("a")
        chapter_links.append(link.get('href'))

    chapter_links.reverse()

    for j in range(len(chapter_links)):
        links.append((j, chapter_links[j]))

    return links

#def chapter_links_mangadex(page):
#def image_links_e_hentai(page):

def img_save(target_dir, file_content):
    filename = os.path.join(target_dir, str(file_content[1]) + '-' + str(file_content[2]))
    if not(os.path.isfile(filename)):
        content = requests.get(file_content[0], stream=True)
        with open(filename, 'wb') as f:
            for chunk in content:
                f.write(chunk)

def img_scraper_asura(links, target_dir):
    
    for i in links:
        page = bs4.BeautifulSoup(get_response(i[1]), 'html.parser')

        imgs_list = page.find(id="content").find(class_="wrapper").find(class_="chapterbody").find(class_="postarea").find("article").find("div", class_="entry-content entry-content-single maincontent").find("div", id="readerarea").find_all("p")
        
        img_links=[]
        k = 0
        for j in imgs_list:
            if k == 0:
                k=k+1
                continue
            else:
                a = ''
                b = ''
                if i[0]<10:
                    a = '0'+str(i[0])
                else:
                    a = str(i[0])
                if k<10:
                    b = '0'+str(k)
                else:
                    b = str(k)

                img_links.append((j.find("img").get('src'), a, b))
                k=k+1
        
        for j in img_links:
            img_save(target_dir, j)

        print("Link: ", i[1], "complete")

#site = "https://asuratoon.com/manga/1908287720-i-shall-live-as-a-prince/"
#target_dir = "/home/marion/Pictures/test"

links = chapter_links_asura(get_response(sys.argv[1]))
img_scraper_asura(links, sys.argv[2])
