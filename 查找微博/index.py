from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import os


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def scroll_down():
    html = driver.find_element_by_tag_name('html')

    height = html.size['height']

    extension_height = 0

    while extension_height != height:
        js = f'window.scrollTo(0, document.body.scrollHeight)'
        driver.execute_script(js)

        html = driver.find_element_by_tag_name('html')
        height = extension_height
        extension_height = html.size['height']
        time.sleep(2)


def get_content():
    content = driver.find_elements_by_css_selector('div.WB_text')
    for i in content:
        print(i.text)


url = 'https://weibo.com/starcraft?refer_flag=0000015010_&from=feed&loc=nickname&is_all=1'

driver = start_chrome()
driver.get(url)

time.sleep(5)

# 翻到底
scroll_down()

get_content()

# 获取下一页
# next = driver.find_element_by_css_selector('a.page.next')

