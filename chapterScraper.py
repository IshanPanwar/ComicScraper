import bs4
import webHandler

class chapter_names:
    def __init__(self, page):
        self.page = page

    def links(self, link):
        match webHandler.linkType(link):
            case "asura":
                return self.asura_links()
            case "mangadex":
                print("Mangadex currently not supported")
                exit(1)
#                return self.mangadex_scraper()
            case None:
                print("Website not supported!")
                exit(1)

    def asura_links(self):
        text = bs4.BeautifulSoup(self.page, 'html.parser')

        chapters = text.find(id="chapterlist").find(class_="clstyle")
        li = chapters.find_all("li")
        chapter_links = []

        for i in li:
            link = i.find("div", class_="chbox").find("div", class_="eph-num").find("a")
            chapter_links.append(link.get('href'))

        chapter_links.reverse()

        for j in range(len(chapter_links)):
            link = chapter_links[j]
            chapter_links[j] = (j, chapter_links[j])

        return chapter_links
