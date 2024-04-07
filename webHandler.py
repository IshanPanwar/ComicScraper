import requests
import os

def get_response(link):
    response = requests.get(link)
    if response.status_code != 200:
        print("Issues with connecting to website")
        exit(1)
    else:
        response.encoding = "utf-8"
        page = response.text
        return page

def linkType(link):
    if link[8:17] == "asuratoon":
        return "asura"
    elif link[8:15] == "mangadex":
        return "mangadex"
    else:
        return None

def img_save(target_dir, file_content):
    filename = os.path.join(target_dir, str(file_content[1]) + '-' + str(file_content[2]))
    if not(os.path.isfile(filename)):
        content = requests.get(file_content[0], stream=True)
        with open(filename, 'wb') as f:
            for chunk in content:
                f.write(chunk)
