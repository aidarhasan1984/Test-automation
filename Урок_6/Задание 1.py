from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# находим и нажимаем на синюю кнопку
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

# ждем, пока зеленая плашка не появится
green_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
)

# получаем текст из зеленой плашки
text = green_box.text

# выводим его в консоль
print(text)

# закрываем браузер
driver.quit()