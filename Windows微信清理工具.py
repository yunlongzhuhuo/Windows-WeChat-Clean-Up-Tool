import os
import sys
import time
import traceback
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from os import path as p
import ctypes.wintypes
 
def getDocPath(pathID=5):
    '''默认返回我的文档路径，buf为空则返回当前工作路径'''
    buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, pathID, None, 0, buf)
    return p.dirname(p.realpath(__file__)) if buf.value=='' else buf.value


try: # 定位WeChat Files文件夹
    f = open(getDocPath(26) + '\\Tencent\\WeChat\\All Users\\config\\3ebffe94.ini',encoding = 'utf-8')
    f1 = f.read()
    if f1 == 'MyDocument:':
        location = getDocPath() + '\WeChat Files'
    else:
        location = f1 + "\WeChat Files"
    try:
        list0 = os.listdir(location)
        list0.remove('All Users')
        list0.remove('Applet')
        title = "(状态正常)"
        errorcode = 0
    except:
        location = getDocPath(5) + '\WeChat Files'
        list0 = os.listdir(location)
        list0.remove('All Users')
        list0.remove('Applet')
        title = "(状态正常)"
        errorcode = 0
except Exception as reason: 
    title = "(错误)"
    erroreason = '错误原因是: \n' + str(traceback.format_exc())
    showerror(title = 'Windows微信清理工具   yunlongzhuhuo[52pojie.cn]',message = '欢迎使用此工具！\n 很抱歉，WeChat Files文件夹定位失败！ \n 工具不能使用！\n %s \n 请反馈给开发者！' % erroreason)

class Application_ui(Frame): # 生成GUI界面
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Windows微信清理工具' + title + '   yunlongzhuhuo[52pojie.cn]')
        sw = master.winfo_screenwidth() #得到屏幕宽度
        sh = master.winfo_screenheight() #得到屏幕高度
        ww = 621
        wh = 308
        x = (sw-ww) / 2
        y = (sh-wh) / 2
        self.master.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
        self.createWidgets()

    def createWidgets(self):
        try:
            self.top = self.winfo_toplevel()

            self.style = Style()

            self.Command1Var = StringVar(value='清理')
            self.style.configure('TCommand1.TButton', font=('微软雅黑',10))
            self.Command1 = Button(self.top, text='清理', textvariable=self.Command1Var, command=self.cleaner, style='TCommand1.TButton')
            self.Command1.setText = lambda x: self.Command1Var.set(x)
            self.Command1.text = lambda : self.Command1Var.get()
            self.Command1.place(relx=0.386, rely=0.701, relwidth=0.195, relheight=0.159)

            self.Combo2List = ('聊天记录','图片和视频','接收到的文件','30天前的图片和视频','30天前接收到的文件','全部数据')
            self.Combo2Var = StringVar(value='')
            self.Combo2 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo2Var, values=self.Combo2List, font=('微软雅黑',9))
            self.Combo2.setText = lambda x: self.Combo2Var.set(x)
            global choice
            choice = lambda : self.Combo2Var.get()
            self.Combo2.place(relx=0.412, rely=0.416, relwidth=0.53)

            global list0
            self.Combo1List = tuple(list0)
            self.Combo1Var = StringVar(value='')
            self.Combo1 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('微软雅黑',9))
            self.Combo1.setText = lambda x: self.Combo1Var.set(x)
            global wxid
            wxid = lambda : self.Combo1Var.get()
            self.Combo1.place(relx=0.412, rely=0.13, relwidth=0.53)

            self.Label2Var = StringVar(value='请选择你要清理的内容：')
            self.style.configure('TLabel2.TLabel', anchor='center', font=('微软雅黑',10))
            self.Label2 = Label(self.top, text='请选择你要清理的内容：', textvariable=self.Label2Var, style='TLabel2.TLabel')
            self.Label2.setText = lambda x: self.Label2Var.set(x)
            self.Label2.text = lambda : self.Label2Var.get()
            self.Label2.place(relx=0.063, rely=0.416, relwidth=0.248, relheight=0.065)

            self.Label1Var = StringVar(value='请选择你要清理的微信号：')
            self.style.configure('TLabel1.TLabel', anchor='center', font=('微软雅黑',10))
            self.Label1 = Label(self.top, text='请选择你要清理的微信号：', textvariable=self.Label1Var, style='TLabel1.TLabel')
            self.Label1.setText = lambda x: self.Label1Var.set(x)
            self.Label1.text = lambda : self.Label1Var.get()
            self.Label1.place(relx=0.052, rely=0.13, relwidth=0.271, relheight=0.065)

            global errorcode
            errorcode = 0
        except Exception as reason:
            errorcode = 1
            erroreason = '错误原因是: \n' + str(traceback.format_exc())

        if errorcode == 0:
            showinfo(title = 'Windows微信清理工具   yunlongzhuhuo[52pojie.cn]',message = '欢迎使用此工具！\n WeChat Files文件夹定位成功: %s \n 工具可以正常使用！' % location)
        if errorcode == 1:
            showerror(title = 'Windows微信清理工具   yunlongzhuhuo[52pojie.cn]',message = '欢迎使用此工具！\n 很抱歉，tkinter界面生成失败！ \n 工具不能使用！\n %s \n 请反馈给开发者！' % erroreason)

    def cleaner(self):

        def delete(files): # 清空文件夹函数
            ask = askokcancel(title = 'Windows微信清理工具',message = '确认清理？')
            if ask == True:
                result0 = os.popen('del /f /s /q "%s\\*.*"' % files)
                result00 = result0.read()
                showinfo(title = 'Windows微信清理工具',message = '清理成功！清理内容:\n%s' % result00)

        def del_time_item(locations): # 删除文件函数
            global asked
            if asked == True:
                global result1
                result1 = os.popen('del /f /s /q "%s"' % locations)
                global result11
                result11 = result1.read()
                global result
                result = True

        def timecleaner(fileslocation): # 遍历查找30天前的文件并删除
            try:
                nowtime = time.time()
                os.chdir(fileslocation) 
                for root, dirs, files in os.walk(fileslocation):
                    for file in files:
                        fileslist = []
                        fileslist.append(os.path.join(root,file))
                        for fileslist1 in fileslist:
                            filestime = os.path.getmtime(fileslist1)
                            timelist = []
                            time_until_now = nowtime - filestime
                            timelist.append(time_until_now)
                            dict0 = dict(zip(fileslist,timelist))
                            if time_until_now < 2592000:
                                timelist.remove(time_until_now)
                            for delitem in timelist:    
                                delfile = list(dict0.keys())[list(dict0.values()).index(delitem)]
                                del_time_item(delfile)
            except Exception as reason:
                showerror(title = 'Windows微信清理工具',message = '出错啦~~ \n 错误原因是：\n %s \n 请反馈给开发者！' % traceback.format_exc())
                

        def getwxid(): # 获得微信号
            return wxid()

        def getchoice(): # 获得路径
            return choice()

        if getchoice() == '聊天记录':           # 具体删除功能
            dialog = location + "\\" + getwxid() + '\Msg'
            delete(dialog)
        elif getchoice() == '图片和视频':
            pictures = location + "\\" + getwxid() + '\FileStorage\Image'
            delete(pictures)
            videos = location + "\\" + getwxid() + '\FileStorage\Video'
            delete(videos)
        elif getchoice() == '接收到的文件':
            documents = location + "\\" + getwxid() + '\FileStorage\File'
            delete(documents)
        elif getchoice() == '全部数据':
            delall = location + "\\" + getwxid()
            delete(delall)
        elif getchoice() == '30天前的图片和视频':
            pictures = location + "\\" + getwxid() + '\FileStorage\Image'
            videos = location + "\\" + getwxid() + '\FileStorage\Video'
            global asked
            asked = askokcancel(title = 'Windows微信清理工具',message = '确认清理？')
            timecleaner(pictures)
            timecleaner(videos)
            try:   
                global result
                if result == True:
                    showinfo(title = 'Windows微信清理工具',message = '清理成功！清理内容:\n%s' % result11)
            except NameError:
                showinfo(title = 'Windows微信清理工具',message = '没有需要清理的文件！')
        elif getchoice() == '30天前接收到的文件':
            documents = location + "\\" + getwxid() + '\FileStorage\File'
            asked = askokcancel(title = 'Windows微信清理工具',message = '确认清理？')
            timecleaner(documents)
            try:
                if result == True:
                    showinfo(title = 'Windows微信清理工具',message = '清理成功！清理内容:\n%s' % result11)
            except NameError:
                showinfo(title = 'Windows微信清理工具',message = '没有需要清理的文件！')

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
