import itchat
import csv

# 登录微信
itchat.auto_login(hotReload=True)

# 获取所有微信群聊
chatrooms = itchat.get_chatrooms()

# 打印所有微信群聊，并选择一个微信群聊
print("当前微信群聊列表：")
for index, room in enumerate(chatrooms):
    print(f"{index}. {room['NickName']}")

room_index = int(input("请输入要导出的微信群聊编号："))
target_room = chatrooms[room_index]

# 获取指定微信群的成员列表
members = itchat.update_chatroom(target_room['UserName'], detailedMember=True)['MemberList']

# 打印微信群成员
for member in members:
    print(f"{member['NickName']} ({member['UserName']})")

# 导出成员列表到CSV文件
with open('wechat_group_members.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['NickName', 'UserName'])
    for member in members:
        writer.writerow([member['NickName'], member['UserName']])

print("微信群成员列表已导出到 wechat_group_members.csv 文件。")

# 登出微信
itchat.logout()