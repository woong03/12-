 import sys
sys.path.insert(0, '/user/lib/chromium-browser/chromedriver')
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

genre = input('장르를 선택하세요 가요 = 1, POP = 2, JPOP = 3  ')
year1, month1, date1, year2, month2, date2 = map(int,input(f'??년 ??월 ??일 ~ ??년 ??월 ??일  ').split())

#장르 선택
search_genre = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[1]/li/select/option[{genre}]')
search_genre.click()
#시작 날짜 선택
search_start_year = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[2]/li/select/option[{year1-2019}]')
search_start_year.click()
search_start_month = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[3]/li/select/option[{month1}]')
search_start_month.click()
search_start_date = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[4]/li/select/option[{date1}]')
search_start_date.click()
#끝 날짜 선택
search_end_year = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[6]/li/select/option[{year2-2019}]')
search_end_year.click()
search_end_month = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[7]/li/select/option[{month2}]')
search_end_month.click()
search_end_date = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[8]/li/select/option[{date2}]')
search_end_date.click()


search = browser.find_element_by_xpath(f'//*[@id="searchPopular"]/form/ul[9]/li/a/img')
search.click()

for i in range(2,102):
  grade = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[1]').text
  number = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[2]').text
  title = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[3]').text
  artist = browser.find_element_by_xpath(f'//*[@id="BoardType1"]/table/tbody/tr[{i}]/td[4]').text
  print(grade, number, title, artist)
