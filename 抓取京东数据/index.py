from selenium import webdriver
import time
import json

url = 'https://item.jd.com/5463278.html'
name = "索尼（SONY）WI-1000X Hi-Res颈挂式 入耳式 无线蓝牙耳机"


def start_chrome():
    d = webdriver.Chrome(executable_path='./chromedriver')
    d.start_client()
    return d


def find_strangers():
    btn_sel = 'div#detail > div.tab-main ul > li'
    el = driver.find_elements_by_css_selector(btn_sel)
    return el


driver = start_chrome()
driver.get(url)

text = find_strangers()
for i in text:
    if i.text == "规格与包装":
        i.click()
        time.sleep(2)


def find_status():
    btn_sel = 'div.Ptable-item'
    el = driver.find_elements_by_css_selector(btn_sel)
    return el


def find_kv(h3):
    pass

item = find_status()
dict1 = {'name': '耳机'}
d = {}
for i in item:

    h3 = i.find_element_by_css_selector('h3')
    print(h3.text)

    dts = i.find_elements_by_css_selector('dl > dt')
    dds = i.find_elements_by_css_selector('dl > dd')

    subd = {}
    for index in range(len(dts)):
        print(dts[index].text, dds[index].text)
        subd[dts[index].text] = dds[index].text

    array = [subd]

    d[h3.text] = array

data = json.dumps(d)


fileObject = open(f'{name}.json', 'w')
fileObject.write(data)
fileObject.close()
