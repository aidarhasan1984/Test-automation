from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


chrome_driver_path = "путь_к_вашему_драйверу_chrome"
chrome_driver = webdriver.Chrome(chrome_driver_path)
chrome_driver.get("http://the-internet.herokuapp.com/entry_ad")
time.sleep(2)  

close_button = chrome_driver.find_element_by_css_selector(".modal-footer p")
close_button.click()
time.sleep(2)  

chrome_driver.quit()

firefox_driver_path = "путь_к_вашему_драйверу_firefox"
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path)
firefox_driver.get("http://the-internet.herokuapp.com/entry_ad")
time.sleep(2)  

close_button = firefox_driver.find_element_by_css_selector(".modal-footer p")
close_button.click()
time.sleep(2)  

firefox_driver.quit()