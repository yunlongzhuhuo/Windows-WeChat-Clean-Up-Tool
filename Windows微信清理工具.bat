@echo off
title Windows微信清理工具        by:yunlongzhuhuo
color 1F
echo.
echo -----------------------------Windows微信清理工具-------------------------------------
echo.
echo ------------------------------【1.清理聊天记录】---------------------------------
echo.
echo -----------------------------【2.清理图片和视频】-----------------------------------
echo.
echo -----------------------------【3.清理接收到的文件】------------------------------
echo.
echo ------------------------------【4.清理全部数据】-------------------------------
echo.
set /p input=请输入要执行的操作所对应的代码：
if "%input%"=="1" goto history
if "%input%"=="2" goto pictures
if "%input%"=="3" goto files
if "%input%"=="4" goto all
:history
set /p wxid=请输入你的微信号：
cd %userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config
set /p location=<./3ebffe94.ini
if "%location%"=="MyDocument:" goto first
if "%location%" neq "MyDocument:" goto second
:first
del /f /s /q "%userprofile%\Documents\WeChat Files\%wxid%\Msg\*.*"
echo 清理成功！
pause
:second
del /f /s /q "%location%\WeChat Files\%wxid%\Msg\*.*"
echo 清理成功！
pause
:pictures
set /p wxid=请输入你的微信号：
cd %userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config
set /p location=<./3ebffe94.ini
if "%location%"=="MyDocument:" goto first
if "%location%" neq "MyDocument:" goto second
:first
del /f /s /q "%userprofile%\Documents\WeChat Files\%wxid%\FileStorage\Image\*.*"
del /f /s /q "%userprofile%\Documents\WeChat Files\%wxid%\FileStorage\Video\*.*"
echo 清理成功！
pause
:second
del /f /s /q "%location%\WeChat Files\%wxid%\FileStorage\Image\*.*"
del /f /s /q "%location%\WeChat Files\%wxid%\FileStorage\Video\*.*"
echo 清理成功！
pause
:files
set /p wxid=请输入你的微信号：
cd %userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config
set /p location=<./3ebffe94.ini
if "%location%"=="MyDocument:" goto first
if "%location%" neq "MyDocument:" goto second
:first
del /f /s /q "%userprofile%\Documents\WeChat Files\%wxid%\FileStorage\File\*.*"
echo 清理成功！
pause
:second
del /f /s /q "%location%\WeChat Files\%wxid%\FileStorage\File\*.*"
echo 清理成功！
pause
:all
set /p wxid=请输入你的微信号：
cd %userprofile%\AppData\Roaming\Tencent\WeChat\All Users\config
set /p location=<./3ebffe94.ini
if "%location%"=="MyDocument:" goto first
if "%location%" neq "MyDocument:" goto second
:first
del /f /s /q "%userprofile%\Documents\WeChat Files\%wxid%\*.*"
rd "%userprofile%\Documents\WeChat Files\%wxid%"
echo 清理成功！
pause
:second
del /f /s /q "%location%\WeChat Files\%wxid%\*.*"
rd "%location%\WeChat Files\%wxid%"
echo 清理成功！
pause