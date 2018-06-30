from wxpy import *
import time


def find_group(bot, group_name):
    try:
        groups = bot.groups.search(group_name)
        if len(groups) == 1:
            return groups[0]
        else:
            print("监测失败！未发现群或存在多个名称相同的群。")
            return None
    except ResponseError as e:
        print(e.err_msg)


def get_group_number(group_name):
    try:
        return group_name.member
    except ResponseError as e:
        print(e.err_msg)


def parse_groups(current_group, last_group):

    quit_member = [q.name for last in last_group if last not in current_group]

    new_list = [n.name for cur in current_group if cur not in last_group]

    return "退群名单：" + "，".join(quit_member) + "\n" + "进群名单：" + "，".join(new_list)


# 将指定的消息发送给指定的人
def send_msg(bot, my_name, text):
    try:
        myself = bot.friends().search(my_name)[0]
        myself.send(text)
    except ResponseError as e:
        print(e.err_code, e.err_msg)


def main(my_name, group_name):
    bot = Bot()
    group = find_group(bot, group_name)
    last_member = get_group_number(group)

    while True:
        time.sleep(3600)
        cur_member = get_group_number(group)
        msg = parse_groups(cur_member, last_member)
        send_msg(bot, my_name, msg)
        last_member = cur_member


main("我是五高你是谁", "贺川")

