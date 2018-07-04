# A simple script to scrape URLs to lyrics from https://genius.com/tags/arabic-rap/all

import re
import io
import time

from bs4 import BeautifulSoup
from selenium import webdriver

mybrowser = webdriver.Firefox(executable_path="../../../../../../usr/bin/geckodriver")

url = "https://genius.com/tags/arabic-rap/all"
mybrowser.get(url)

html = mybrowser.page_source

t_sec = time.time() + 60*20 # seconds*minutes #for test purposes use the line beneath
#t_sec = time.time() + 20 #change this time later on to something like the above
while(time.time()<t_sec):
    mybrowser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    html = mybrowser.page_source

soup = BeautifulSoup(html, "html.parser")

pattern = re.compile("[\S]+-lyrics$") # Filter http links that end with "lyrics".

with io.open('list_of_URLs.txt', 'a', encoding='utf8') as myfile:
    for link in soup.find_all('a',href=True):
        if pattern.match(link['href']):
            myfile.write(str(link['href'])+"\n")

mybrowser.close()
myfile.close()



