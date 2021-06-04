import os

import ctypes, win32com.shell.shell, win32event, win32process, os, sys

def wifi():

    os.system("netsh interface show interface")

    def enable(wifi):
        os.system(f"netsh interface set interface {wifi} enabled")

    def disable(wifi):
        os.system(f"netsh interface set interface {wifi} disabled")

    d = input("sdsd >> ")

    disable(d)
    enable(d)

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    wifi()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


