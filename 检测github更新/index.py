import requests
import webbrowser
import time

api = 'https://api.github.com/repos/channelcat/sanic'
web_page = 'https://github.com/channelcat/sanic'

last_update = '2018-06-03T03:35:03Z'

while True:

    all_info = requests.get(api).json()

    cur_update = all_info['updated_at']

    if not last_update:
        last_update = cur_update

    if cur_update > last_update:
        webbrowser.open(web_page)
        last_update = cur_update
    time.sleep(6000)