"""
  created by IAmFiveHigh on 2018-09-27
 """

from selenium import webdriver
import time, random, re, string

count = 5
url = 'http://micro.51.com/client/reg/hy'


def start_chrome():
    d = webdriver.Chrome(executable_path='./chromedriver')
    d.start_client()
    return d


def find_username():
    btn_sel = 'input#username'
    el = driver.find_element_by_css_selector(btn_sel)
    return el


def find_password():
    btn_sel = 'input#password'
    el = driver.find_element_by_css_selector(btn_sel)
    return el


def find_password2():
    btn_sel = 'input#password_2'
    el = driver.find_element_by_css_selector(btn_sel)
    return el


def find_btn():
    btn_sel = 'p.bd_zc > a'
    el = driver.find_element_by_css_selector(btn_sel)
    return el

driver = start_chrome()


def create_password(count):
    passwords = []
    i=0
    while i < count:
        tmp = random.sample(string.ascii_letters + string.digits, 8)
        pd = ''.join(tmp)
        if re.search('[0-9]', pd) and re.search('[A-Z]', pd) and re.search('[a-z]', pd):
            passwords.append(pd)
            i += 1
    return passwords


def create_username(count):
    usernames = []
    i=0
    while i<count:
        tmp = random.sample(string.digits, 9)
        un = ''.join(tmp)
        un = 'qq' + un
        usernames.append(un)
        i += 1
    return usernames

username = create_username(count)
password = create_password(count)

for i in range(count):

    driver.get(url)
    time.sleep(2)

    username_input = find_username()
    password_input = find_password()
    repeat_input = find_password2()

    btn = find_btn()

    username_input.send_keys(username[i])
    password_input.send_keys(password[i])
    repeat_input.send_keys(password[i])
    btn.click()
    print(f'username = {username[i]}, password = {password[i]}')
    time.sleep(5)
    driver.delete_all_cookies()

