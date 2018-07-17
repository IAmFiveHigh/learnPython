from selenium import webdriver
import time
url = 'https://weibo.com/ttarticle/p/show?id=2309404261714949446590#_loginLayer_1531818247829'


# span.pos > span.line.S_line1 > span > em:nth-child(2)
def star_chorme():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def find_info():
    sel = 'span.pos > span.line.S_line1 > span >em'
    elements = driver.find_element_by_css_selector(sel)
    return elements


driver = star_chorme()
driver.get(url=url)
time.sleep(6)
element = find_info()

print(f'该微博点赞数{element.text}')