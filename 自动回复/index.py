from wxpy import *
import time

bot = Bot()

count = 0
while True:

    time.sleep(2)

    message = bot.messages

    if len(message) > count:

        last_message = message[-1]
        count = len(message)
        # if not last_message.chat == "李贺川" and not last_message.member:
        #     last_message.chat.send("您好 我是五高的自动回复机器人，他可能在忙，一会儿就回复您，请耐心等待")
        if last_message.text == "我爱你":
            last_message.chat.send("我也爱你")
            
        if last_message.text == "再见":
            last_message.chat.send("拜拜")

        if last_message.text == "苟利国家生死以":
            last_message.chat.send("岂因祸福避趋之")

    else:
        pass



