from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "путь_к_chrome"
chrome_driver = webdriver.Chrome(chrome_driver_path)
chrome_driver.get("http://the-internet.herokuapp.com/inputs")
time.sleep(2) 

input_field = chrome_driver.find_element_by_tag_name("input")
input_field.send_keys("1000")
time.sleep(1) 

input_field.clear()
time.sleep(1)

input_field.send_keys("999")
time.sleep(1)

chrome_driver.quit()

# Для Firefox
firefox_driver_path = "путь_к_firefox"
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path)
firefox_driver.get("http://the-internet.herokuapp.com/inputs")
time.sleep(2) 

input_field = firefox_driver.find_element_by_tag_name("input")
input_field.send_keys("1000")
time.sleep(1)  

input_field.clear()
time.sleep(1) 

input_field.send_keys("999")
time.sleep(1)

firefox_driver.quit()