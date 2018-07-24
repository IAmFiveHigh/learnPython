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
    content = driver.find_elements_by_css_selector('div.WB_detail')
    list = []
    for i in content:
        date = i.find_element_by_css_selector('div.WB_from > a.S_txt2').text
        text = i.find_element_by_css_selector('div.WB_text').text
        l = [date, text]
        list.append(l)

    return list


def save(list, name):
    full_path = f'./{name}.csv'
    if os.path.exists(full_path):
        with open(full_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(list)
    else:
        with open(full_path, 'w+') as f:
            whiter = csv.writer(f)
            whiter.writerows(list)

url = 'https://weibo.com/starcraft?refer_flag=0000015010_&from=feed&loc=nickname&is_all=1'

driver = start_chrome()
driver.get(url)

time.sleep(5)

# 翻到底
scroll_down()

# 获取内容
content = get_content()
print(content)
save(content, "星际争霸的微博")


# 获取下一页
# next = driver.find_element_by_css_selector('a.page.next')

