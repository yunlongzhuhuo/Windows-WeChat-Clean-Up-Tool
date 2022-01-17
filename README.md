# Windows-WeChat-Clean-Up-Tool
对Windows中的WeChat Files文件夹进行定位，查找其中的部分数据进行删除操作，达到清理目的。
# 设计思路：
  本工具采用Windows批处理（bat）编写，列出菜单，通过if语句让用户来决定删除哪些数据。然后读取“%userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config\3ebffe94.ini”中的文件路径来定位到WeChat Files的路径，进行删除操作。
