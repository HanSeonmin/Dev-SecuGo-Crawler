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
#driver.find_element_by_css_selector('button.search_btn').click()

### implicit waits
driver.implicitly_wait(10)

### click "더보기"
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()