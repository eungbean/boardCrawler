import requests
import os
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup

#CONFIG
with open('config.json') as config_file:
    config = json.load(config_file)

chrome_version = config["chrome_version"]
OS = config["OS"]
TARGET_URL = "https://www.dogdrip.net/dogdrip"
LOGIN_FORM = config["LOGIN_FORM"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "output")
# LOGIN_URL = 'http://member.newhosting.ssem.or.kr/dggb/mber/mberLogin/actionMberLogin.do'

########################WEBDRIVER#########################
#what OS do you use?
if (OS=='mac'):
    PATHcrawler = os.path.join(BASE_DIR,'src','chrome'+chrome_version,'chromedriver-mac')
elif (OS=='win'):
    PATHcrawler = os.path.join(BASE_DIR,'src','chrome'+chrome_version,'chromedriver.exe')
elif (OS=='linux'):
    PATHcrawler = os.path.join(BASE_DIR,'src','chrome'+chrome_version,'chromedriver-linux')
else :
    print("write correct os")

########################HACKS#########################
print("Configuration Driver ..")

#Chrome Config
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

print("Avioding Healess Detection ..")
startTime = time.time()

# Headless 탐지 방어
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR") # 한국어!

driver = webdriver.Chrome(PATHcrawler, options=options)
driver.implicitly_wait(1)

# endTime = time.time() - startTime
# print("Avioding Healess Detection DONE: {} seconds".format(endTime))
# # Headless 탐지 방어 : 가짜 플러그인 주입
# print("Injecting Fake Plugins ..")
# startTime = time.time()

# driver.get('about:blank')
# driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

# endTime = time.time() - startTime
# print("Injecting Fake Plugins DONE: {} seconds".format(endTime))
########################CRAWLER#########################
print("Initialize Crawing Driver ..")
startTime = time.time()

# URL 접속해서 response 파싱하기
outs = driver.get(TARGET_URL)

#Beutifulsoap
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') 
# containers = soup.select("#main > div > div.eq.section.secontent.background-color-content > div > div.ed.board-list > table > tbody > tr")
containers = soup.select("#main > div > div.eq.section.secontent.background-color-content > div > div.ed.board-list > table > tbody > tr > td > a")

# > tr:nth-child(3) > td.title > a

endTime = time.time() - startTime
print("Initialize Crawing Driver DONE: {} seconds".format(endTime))
print("Start CRAWLING")
startTime = time.time()
# JSON으로 저장
items = []
for container in containers:
    items.append({
        'num': container.get_text(strip=True),
        # 'title': container.select('a > span')[0].get_text(strip=True),
        'href': container.get('href'),#.get_text(strip=True),
        # 'date': container[4].get_text(strip=True),
        # 'author': container[2].get_text(strip=True),
        # 'upvotes': container[3].get_text(strip=True)
    })
    # print("GET: ", container.select('tr').get_text(strip=True))

# for container in containers:
#     items.append({
#         'num': container.select('td')[0].get_text(strip=True),
#         'title': container.select('td > a > span')[0].get_text(strip=True),
#         'href': container.get('href'),#.get_text(strip=True),
#         'date': container.select('td')[4].get_text(strip=True),
#         'author': container.select('td')[2].get_text(strip=True),
#         'upvotes': container.select('td')[3].get_text(strip=True)
#     })
#     # print("GET: ", container.select('tr').get_text(strip=True))
#     time.sleep(0.1)

endTime = time.time() - startTime
print("CRAWLING DONE: {} seconds".format(endTime))
startTime = time.time()

# JSON으로 저장
with open(os.path.join(OUT_DIR, 'result.json'), "w") as writeJSON:
   json.dump(items, writeJSON,  indent=4, ensure_ascii=False)

# #제목만 저장
# with open(os.path.join(OUT_DIR, 'subjects.txt'), 'w+') as f:
#     for item in items:
#         f.write(item['title']+"\n")

# endTime = time.time() - startTime
# print("SAVING DONE: {} seconds".format(endTime))

#LOGIN WITH REQUEST
# with requests.Session() as s:
#    login_req = s.post(LOGIN_URL, data=LOGIN_FORM)#, value = "success")
#    print(login_req.status_code) # 200: success
