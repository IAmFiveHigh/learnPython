from selenium import webdriver
import time
import json

str = """100001332626
    33743197985"""

l = str.split('\n')


def start_chrome():
    d = webdriver.Chrome(executable_path='./chromedriver')
    d.start_client()
    return d


def find_strangers():
    btn_sel = 'div#detail > div.tab-main ul > li'
    el = driver.find_elements_by_css_selector(btn_sel)
    return el


def find_status():
    btn_sel = 'div.Ptable-item'
    el = driver.find_elements_by_css_selector(btn_sel)
    return el


def find_name():
    btn_sel = 'div.sku-name'
    el = driver.find_element_by_css_selector(btn_sel)
    return el.text


driver = start_chrome()
for i in l:
    sku = i
    url = f'https://item.jd.com/{sku}.html'
    
    driver.get(url)
    
    text = find_strangers()
    for i in text:
        if i.text == "规格与包装":
            i.click()
            time.sleep(2)

item = find_status()
d = []
for i in item:
    
    h3 = i.find_element_by_css_selector('h3')
    print(h3.text)
    # Ptable - tips
    dts = i.find_elements_by_css_selector('dl > dt')
        
        temp = i.find_element_by_css_selector('dl')
        # dds = temp.find_elements_by_xpath('//dd[not(contains(@class, "Ptable - tips"))]')
        dds = i.find_elements_by_css_selector('dl > dd')
        dds_not = temp.find_elements_by_class_name("Ptable-tips")
        
        for dd in dds:
            if dd in dds_not:
                dds.remove(dd)
        subd = []
        for index in range(len(dts)):
            print(dts[index].text, dds[index].text)
            sub_result = {"key": dts[index].text, "value": dds[index].text}
            subd.append(sub_result)

    dic = {'h1': h3.text, 'list': subd}
        d.append(dic)

data = json.dumps(d).encode('utf-8').decode('unicode_escape')

name = find_name().strip()[0:20]
print(name)
fileObject = open(f'{name}.txt', 'w')
fileObject.write(data)
fileObject.close()

time.sleep(4)
