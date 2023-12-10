from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_driver_path = "путь_к_chrome"
chrome_driver = webdriver.Chrome(chrome_driver_path)
chrome_driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(2)  

blue_button = chrome_driver.find_element_by_id("colorVar")
blue_button.click()

time.sleep(3) 

firefox_driver_path = "путь_к _firefox"
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path)
firefox_driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(2)  

blue_button = firefox_driver.find_element_by_id("colorVar")
blue_button.click()

time.sleep(3)  

chrome_driver.quit()
firefox_driver.quit()