import requests
import time
import webbrowser

api = "https://api.github.com/users/{}/starred".format("cnzhangbin")

json_response = requests.get(api).json()

starred = []

for i in json_response:
    starred.append(i['id'])


while True:
    info = requests.get(api).json()
    for i in info:
        if not i['id'] in starred:
            starred.append(i['id'])
            repo_name = i['name']
            # 获取作者名称
            owner = i['owner']['login']
            # 在浏览器中打开项目
            web_page = "https://github.com/" + owner + "/" + repo_name
            webbrowser.open(web_page)

    time.sleep(6000)