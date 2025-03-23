@echo off
REM 激活虚拟环境
call .\stvenv\Scripts\activate.bat

REM 检查是否成功激活虚拟环境
if errorlevel 1 (
    echo 虚拟环境激活失败，请检查路径是否正确。
    pause
    exit /b
)

REM 运行 Python 脚本
python start_server.py

REM 检查 Python 脚本是否成功运行
if errorlevel 1 (
    echo Python 脚本运行失败。
    pause
    exit /b
)

pause