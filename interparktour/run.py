from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ### for waits
from selenium.webdriver.support import expected_conditions as EC ### for waits

import time
import sys
import pymysql as my

from TourInfo import TourInfo
from DB_config import DBHelper as DB
### load advanced data
base_url = "http://tour.interpark.com/"

keyword = "체코"
db = DB()

### load driver
driver = wd.Chrome(executable_path='/usr/local/bin/chromedriver')
# TODO: remove temporary file, manage agent,

### access site [GET]
driver.get(base_url)

### forceful waits
time.sleep(1)

### access search bar & input text
driver.find_element_by_id("SearchGNBText").send_keys(keyword)

### click search button
driver.find_element_by_css_selector('.search-btn').click() 
print("CLICK SEARCH BUTTON")
#driver.find_element_by_css_selector('button.search_btn').click()

### implicit waits
driver.implicitly_wait(10)

### click "더보기" -> access tour list
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()
print("CLICK 'MORE'")

### implicit waits
driver.implicitly_wait(10)

### access 3rd tour detail board
third_tour = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')[2]
##### pre-process link text
print(third_tour.find_element_by_css_selector('a').get_attribute('onclick'))
tmp_strs = third_tour.find_element_by_css_selector('a').get_attribute('onclick').split(',')
if tmp_strs:
    third_link = tmp_strs[0].replace('searchModule.OnClickDetail(', '')[1:-1]
print(third_link)
driver.get(third_link)

### implicit waits
driver.implicitly_wait(10)

### print third detail board info
print("t_title:::", driver.find_element_by_css_selector('.default-section>h2>strong').text)
print("t_grade:::", driver.find_element_by_css_selector('.info-section>.score>.point01').text)
print("t_period:::", driver.find_element_by_css_selector('.period>td>strong').text)
print("t_image:::", driver.find_element_by_id('btnThumb_3').find_element_by_css_selector('img').get_attribute('src'))
print("t_content:::", driver.find_elements_by_css_selector('.info-list>.goods-point>.ui-con-list>li')[2].text)

t_content = ""
t_strs = driver.find_elements_by_css_selector('.info-list>.goods-point>.ui-con-list>li')
for t_str in t_strs:
    t_content += (t_str.text + '\n')

print(t_content)

t_obj = TourInfo(
    t_title = driver.find_element_by_css_selector('.default-section>h2>strong').text,
    t_grade = driver.find_element_by_css_selector('.info-section>.score>.point01').text,
    t_period = driver.find_element_by_css_selector('.period>td>strong').text,
    t_image = driver.find_element_by_id('btnThumb_3').find_element_by_css_selector('img').get_attribute('src'),
    t_content = t_content
)
db.insertCrawlingData(t_obj)

# 프로그램 종료
driver.close()
driver.quit()
sys.exit()