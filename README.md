# Windows微信清理工具
对Windows中的WeChat Files文件夹进行定位，查找其中的部分数据进行删除操作，达到清理目的。
## 所有版本及源码下载链接：
### 百度网盘：https://pan.baidu.com/s/1OSIpvZEOvd-lVZb_82BnKg
### 提取码：ylzh
### 阿里云盘：https://www.aliyundrive.com/s/oqCZpgz5WzL
**（希望大家先保存到自己的网盘里再下载，非常感谢）**
# 设计思路：
### bat版本：
  本工具采用Windows批处理（bat）编写。程序先列出菜单，通过if语句让用户来决定删除哪些数据。然后读取“%userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config\3ebffe94.ini”中的文件路径来定位到WeChat Files的路径，进行删除操作。
### Python版本：
  本工具采用Python编写，GUI使用了tkinter。程序先读取“%userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config\3ebffe94.ini”，确定WeChat Files文件夹的位置，进行扫描，列出所有登陆过的微信号，让用户选择需要清理的账号，再列出菜单，通过if语句让用户来决定删除哪些数据，最后进行删除操作。
