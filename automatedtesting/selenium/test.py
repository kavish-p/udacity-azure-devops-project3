from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import datetime


def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')

def login(user, password):
    print(timestamp() + 'Starting Chrome instance.')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options, executable_path='/snap/bin/chromium.chromedriver')
    print(timestamp() + 'Navigating to demo website.')
    driver.get('https://www.saucedemo.com/')

    find_web_element(driver, By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    find_web_element(driver, By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    find_web_element(driver, By.ID, "login-button").click()

    product_label = find_web_element(driver, By.CSS_SELECTOR, "#header_container > div.header_secondary_container > span").text
    assert "Products" in product_label
    print(timestamp() + 'Logged with username {:s} and password {:s}'.format(user, password))
    return driver

def add_cart(driver, product_num):
    for i in range(product_num):
        element = "a[id='item_" + str(i) + "_title_link']"
        find_web_element(driver, By.CSS_SELECTOR, element).click()
        find_web_element(driver, By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        product = find_web_element(driver, By.CLASS_NAME, "inventory_details_name").text
        print(timestamp() + product + " added to shopping cart.")
        find_web_element(driver, By.ID, "back-to-products").click()
    print(timestamp() + '{:d} items have been added to shopping cart.'.format(product_num))

def remove_cart(driver, product_num):
    for i in range(product_num):
        element = "a[id='item_" + str(i) + "_title_link']"
        find_web_element(driver, By.CSS_SELECTOR, element).click()
        find_web_element(driver, By.CSS_SELECTOR, "button.btn_secondary.btn_inventory").click()
        product = find_web_element(driver, By.CLASS_NAME, "inventory_details_name").text
        print(timestamp() + product + " removed from shopping cart.")
        find_web_element(driver, By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items have been removed from the shopping cart.'.format(product_num))

def find_web_element(wd, selector_type, selector_value):
    element = WebDriverWait(wd, 20).until(
        EC.visibility_of_element_located((selector_type, selector_value))
    )
    return element

if __name__ == "__main__":
    print("Starting Test Case")
    PRODUCT_NUM = 6
    TEST_USERNAME = 'standard_user'
    TEST_PASSWORD = 'secret_sauce'
    driver = login(TEST_USERNAME, TEST_PASSWORD)
    add_cart(driver, PRODUCT_NUM)
    remove_cart(driver, PRODUCT_NUM)
    print(timestamp() + 'Selenium test has successfully completed!')