!pip install selenium
!apt-get update
!apt install chromium-chromedriver

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver', options=options)

url = 'http://tjmedia.com/tjsong/song_monthPopular.asp'
browser.get(url)

for i in range(2,102):
  grade = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[1]').text
  number = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[2]').text
  title = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[3]').text
  artist = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[4]').text
  print(grade, number, title, artist)
