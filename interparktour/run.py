from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ### for waits
from selenium.webdriver.support import expected_conditions as EC ### for waits

import time
import sys
import pymysql as my

### load advanced data
base_url = "http://tour.interpark.com/"

keyword = "체코"

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

### access 3rd tour detail board
third_tour_info = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')[2]
third_tour_info.find_element_by_css_selector('img').click()
# driver.find_element_by_css_selector('.oTravelBox>.boxList>li')[2].find_element_by_css_selector('img').click()
print("CLICK THIRD DETAIL BOARD IMAGE")



