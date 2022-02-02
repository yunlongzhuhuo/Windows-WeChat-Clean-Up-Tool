import os

def delete(files):
    os.system('del /f /s /q "%s\\*.*"' % files)
    print("清理成功！")
    
users = os.path.expandvars('$HOMEPATH')
f = open(r'C:' + users + '\\AppData\\Roaming\\Tencent\\WeChat\\All Users\\config\\3ebffe94.ini')
if f.read() == 'MyDocument:':
    location = 'C:' + users + '\Documents\WeChat Files'
else:
    location = f.read() + "\WeChat Files"
list = os.listdir(location)
list.remove('All Users')
list.remove('Applet')
print("""
""")
print(list)
print("""
""")
while True:
    temp = input("选择你要清理的微信号：")
    try:
        if 0<int(temp)<=len(list):
            temp1 = int(temp) - 1
            wxid = list[temp1]
            break
        else:
            print("输入错误，请重新输入。")
    except:
        print("输入错误，请重新输入。")
print("""
         -----------------------------Windows微信清理工具-------------------------------------

         ------------------------------【1.清理聊天记录】---------------------------------

         -----------------------------【2.清理图片和视频】-----------------------------------

         -----------------------------【3.清理接收到的文件】------------------------------

         ------------------------------【4.清理全部数据】-------------------------------

         """)
while True:
    choice = input("请输入要执行的操作所对应的代码：")
    if choice == '1':
        dialog = location + "\\" + wxid + '\Msg'
        delete(dialog)
        break
    elif choice == '2':
        pictures = location + "\\" + wxid + '\FileStorage\Image'
        delete(pictures)
        videos = location + "\\" + wxid + '\FileStorage\Video'
        delete(videos)
        break
    elif choice == '3':
        documents = location + "\\" + wxid + '\FileStorage\File'
        delete(documents)
        break
    elif choice == '4':
        delall = location + "\\" + wxid
        delete(delall)
        break
    else:
        print("输入错误，请重新输入。")
