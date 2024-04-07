import bs4
import webHandler

class image_extractor:
    def __init__(links, target):
        self.image_list = links
        self.target = target

    def name_corrector(self, b):
        if b<10:
            a = '00'+str(b)
        elif b=>10 and b<100:
            a = '0'+str(b)
        else:
            a = str(b)
        return a

    def extractor(self):
        match webHandler.linkType(self.image_list[0]):
            case "asura":
                return self.asura_scraper()
            case "mangadex":
                return self.mangadex_scraper()

    def asura_scraper(self):
        img_links=[]
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
                    a = self.name_corrector(i[0])
                    b = self.name_corrector(k)
                    img_links.append((j.find("img").get('src'), a, b))
                    k=k+1

        return img_links
