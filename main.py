from imageExtractor import image_extractor
from chapterScraper import chapter_names
import webHandler
import sys

#site = "https://asuratoon.com/manga/1908287720-i-shall-live-as-a-prince/"
#target_dir = "/home/marion/Pictures/test"

page = webHandler.get_response(sys.argv[1])
links = chapter_names(page).links(sys.argv[1])
img_links = image_extractor(links, sys.argv[2]).extractor()
