from selenium import webdriver
import time


url = 'https://www.zhihu.com/'
followers_url = 'https://www.zhihu.com/people/li-he-chuan/followers'


def start_chrome():
    d = webdriver.Chrome(executable_path='./chromedriver')
    d.start_client()
    return d


def find_strangers():
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    el = driver.find_elements_by_css_selector(btn_sel)
    return el


driver = start_chrome()
driver.get(url)
# with open('./cookie.txt', 'r') as f:
#     driver.add_cookie(f)

time.sleep(20)

# 获取cookie
c = driver.get_cookies()
# with open('./cookie.txt', 'w') as f:
#     f.write(c)
print(c)

driver.get(followers_url)
time.sleep(5)
strangers = find_strangers()
for s in strangers:
    s.click()
    time.sleep(2)
