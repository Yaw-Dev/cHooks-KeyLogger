@echo off

pip install discord discord.embeds keyboard asyncio requests portalocker
cls

:givename
color 0a
echo.
set /p a="Enter the exe name : "
if [%a%]==[] ( 
    cls
    echo.
    color 0c
    echo Error: Invalid or no name was given.
    pause
    cls
    goto givename
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    pyinstaller --noconfirm --onefile --icon "NONE" -n %a% main.pyw
    rmdir /s /q __pycache__
    rmdir /s /q build
    del /f / s /q %a%.spec
    echo.
    echo generated exe as %a%.exe in the dist folder
    echo.
    pause
    EXIT /B 1
)
