def test_slow_calculator(browser):
  
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = browser.find_element_by_id("delay")
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = [
        "7", "operator", "8", "equal"
    ]
    for button in buttons:
        element = browser.find_element_by_class_name(button)
        element.click()

    time.sleep(45)
    result = browser.find_element_by_id("result").text
    assert result == "15"