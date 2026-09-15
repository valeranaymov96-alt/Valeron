import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module") # отработает один раз в модуле
#@pytest.fixture # отработает для каждой функции
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless") # в фоне

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options= chrome_options)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    yield driver
    driver.quit()

@pytest.mark.smoke
def test_open_form(driver):
    tab_title = ("xpath", "//body//h1")
    tab_title_element = driver.find_element(*tab_title)

    assert tab_title_element.text == "Web form"

@pytest.mark.smoke
def test_submit_button_is_visible_and_enabled(driver):
    submit_button = ("xpath", "//button[@type='submit']")
    submit_button_element = driver.find_element(*submit_button)

    assert submit_button_element.is_displayed()
    assert submit_button_element.is_enabled()

@pytest.mark.smoke
def test_text_input_Selenium(driver):
    text_input = ("xpath", "//input[@id='my-text-id']")
    text_input_element = driver.find_element(*text_input)

    text_input_element.clear()
    text_input_element.send_keys("Selenium")

    assert text_input_element.get_attribute("value") == "Selenium"

@pytest.mark.smoke
def test_text_input_Hello(driver):
    text_input = ("xpath", "//input[@id='my-text-id']")
    text_input_element = driver.find_element(*text_input)

    text_input_element.clear()
    text_input_element.send_keys("Hello")

    assert text_input_element.get_attribute("value") == "Hello"

@pytest.mark.smoke
def test_textarea_accepts_two_lines(driver):
    textarea = ("xpath", "//textarea[@name='my-textarea']")
    textarea_element = driver.find_element(*textarea)
    textarea_element.clear()
    textarea_element.send_keys("str1\nstr2\n")

    assert textarea_element.get_attribute("value") == "str1\nstr2\n"

@pytest.mark.smoke
def test_disabled_input(driver):
    disabled_input = ("xpath", "//input[@name='my-disabled']")
    disabled_input_element = driver.find_element(*disabled_input)

    assert not disabled_input_element.is_enabled()

@pytest.mark.smoke
def test_checked_checkbox(driver):
    checked_checkbox = ("xpath", "//input[@id='my-check-1']")
    checkbox_label = ("xpath", "//input[@id='my-check-1']/parent::label")

    checked_checkbox_element = driver.find_element(*checked_checkbox)

    assert checked_checkbox_element.is_selected()

    driver.find_element(*checkbox_label).click()

    assert not checked_checkbox_element.is_selected()
