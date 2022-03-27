from sys import modules
import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv


file = open('fri_webtoon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['title', 'writer', 'rating'])


WEBTOON_URL = "https://comic.naver.com/webtoon/weekdayList?week=fri"
webtoon_html = requests.get(WEBTOON_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

friday_list = webtoon_soup.find("ul", {"class":"img_list"}).find_all("li")

for item in extract_info(friday_list):
    writer.writerow([item['title'], item['writer'], item['rating']])
