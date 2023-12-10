from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

print("Размер списка кнопок Delete:", len(delete_buttons))

driver.quit()

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

print("Размер списка кнопок Delete:", len(delete_buttons))

driver.quit()