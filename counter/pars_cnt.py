from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def pars(my_req):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.avito.ru/")
    name = driver.find_element_by_id('search')
    name.send_keys(my_req)
    driver.find_element_by_class_name('index-button-2q4Wv').click()
    sleep(3)
    counter = driver.find_element_by_class_name('page-title-count-1oJOc')
    return counter.text
