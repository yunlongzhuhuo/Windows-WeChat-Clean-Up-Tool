import os
import easygui as g

def delete(files):
    os.system('del /f /s /q "%s\\*.*"' % files)
    g.msgbox(msg = '清理成功！',title = 'Windows微信清理工具   yunlongzhuhuo[52pojie.cn]',ok_button='OK')

users = os.path.expandvars('$HOMEPATH')
f = open(r'C:' + users + '\\AppData\\Roaming\\Tencent\\WeChat\\All Users\\config\\3ebffe94.ini')
if f.read() == 'MyDocument:':
    location = 'C:' + users + '\Documents\WeChat Files'
else:
    location = f.read() + "\WeChat Files"
list = os.listdir(location)
list.remove('All Users')
list.remove('Applet')
wxid = g.choicebox(msg = '请选择你要清理的微信号：',title = 'Windows微信清理工具   yunlongzhuhuo[52pojie.cn]',choices = list)
choice = g.buttonbox(msg = '请选择你要清理的对象：', title = 'Windows微信清理工具   yunlongzhuhuo[52pojie.cn]', choices = ('聊天记录', '图片和视频', '接收到的文件', '全部数据'))
if choice == '聊天记录':
    dialog = location + "\\" + wxid + '\Msg'
    delete(dialog)
elif choice == '图片和视频':
    pictures = location + "\\" + wxid + '\FileStorage\Image'
    delete(pictures)
    videos = location + "\\" + wxid + '\FileStorage\Video'
    delete(videos)
elif choice == '接收到的文件':
    documents = location + "\\" + wxid + '\FileStorage\File'
    delete(documents)
elif choice == '全部数据':
    delall = location + "\\" + wxid
    delete(delall)
