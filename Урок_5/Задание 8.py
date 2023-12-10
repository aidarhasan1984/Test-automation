from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver = webdriver.Chrome()
chrome_driver.get("http://the-internet.herokuapp.com/login")

username = chrome_driver.find_element_by_id("username")
password = chrome_driver.find_element_by_id("password")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

submit_button = chrome_driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

chrome_driver.implicitly_wait(10)

chrome_driver.quit()

firefox_driver = webdriver.Firefox()
firefox_driver.get("http://the-internet.herokuapp.com/login")

username = firefox_driver.find_element_by_id("username")
password = firefox_driver.find_element_by_id("password")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

submit_button = firefox_driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()

firefox_driver.implicitly_wait(10)

firefox_driver.quit()
