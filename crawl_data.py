import os
import re
import time
import json
import requests
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/encyc.xml?"
client_id = "mxwcqQBBrs_ggTLo7Ihy"
client_secret = "wMuOBLfHqK"
keywords = "컴퓨터"
header = {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret" : client_secret
}

display = 100
start = 1
id_num = 1

dictionary_data = []

while True :
    time.sleep(3)
    print(start)
    response = requests.get(url + "query="+keywords + "&display="+str(display) +"&start="+str(start), headers=header)
    rescode = response.status_code
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    if(rescode == 200) :
        # print(info['items'])
        items = soup.findAll('item')
        # print(items)
        for item in items:
            title = item.title.get_text()
            title = re.sub('<.+?>', '', title, 0).strip()
            content = item.description.get_text()
            content = re.sub('<.+?>', '', content, 0).strip()
            dictionary_data.append({"id" : id_num, "title" : title, "content" : content})
            id_num += 1
    else : 
        print("Error Code : " + rescode)
    start += display
    if start >= 1000 :
        break

with open('C:\\ai\\workspace\\django\\testsite\\dictionary_data.json', 'w', encoding='utf-8') as make_file :
    json.dump(dictionary_data, make_file)