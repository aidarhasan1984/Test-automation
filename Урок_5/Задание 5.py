from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_script(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print('Неправильно указан браузер')
        return

    driver.get('http://uitestingplayground.com/classattr')
    
    button = driver.find_element_by_id('answer4')
    button.click()
    
    driver.quit()

for i in range(3):
    print(f'Запуск скрипта {i+1}')
    run_script('chrome')

for i in range(3):
    print(f'Запуск скрипта {i+1}')
    run_script('firefox')
