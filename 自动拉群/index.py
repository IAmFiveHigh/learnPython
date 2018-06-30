from wxpy import *
import time

bot = Bot()

# 群名
group_name = "test_group"


def lister(pwd):
    time.sleep(5)
    return [msg for msg in bot.messages if msg.text == pwd]


def add_group(users, group):
    try:
        group.add_members(users, use_invitation=True)
        return group
    except ResponseError:
        return None


def add_friend(say):
    return [msg for msg in bot.messages if msg.text == say]


group = bot.groups().search(group_name)[0]

while True:

    print("running")

    new_friend = add_friend("好友")
    if new_friend:
        for friend in new_friend:
            new_user = friend.card
            bot.accept_friend(new_user)
            new_user.send("你好")
            bot.messages.remove(friend)

    time.sleep(5)

    selected = lister("加群")
    if selected:
        for msg in selected:
            this_user = msg.sender
            add_group(this_user, group)
            bot.messages.remove(msg)
