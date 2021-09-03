from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# import chromedriver_binary
browser = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
browser.get('https://finance.yahoo.com/')

search = browser.find_element_by_id('yfin-usr-qry')
search.send_keys("it works!!!")