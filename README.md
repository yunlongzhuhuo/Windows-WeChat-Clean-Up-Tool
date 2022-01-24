# Windows-WeChat-Clean-Up-Tool
对Windows中的WeChat Files文件夹进行定位，查找其中的部分数据进行删除操作，达到清理目的。
# 设计思路：
### bat版本：本工具采用Windows批处理（bat）编写，GUI采用EasyGUI设计。程序先列出菜单，通过if语句让用户来决定删除哪些数据。然后读取“%userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config\3ebffe94.ini”中的文件路径来定位到WeChat Files的路径，进行删除操作。
### Python版本：本工具采用Python编写，GUI使用了EasyGUI。程序先读取“%userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config\3ebffe94.ini”，确定WeChat Files文件夹的位置，进行扫描，列出所有登陆过的微信号，让用户选择清理的对象，再列出菜单，通过if语句让用户来决定删除哪些数据，最后进行删除操作。
