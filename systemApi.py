import ctypes
import os
import subprocess
from errors import WrongOs

def checkAdmin():
    if os.name == 'nt':
        current_process = ctypes.windll.kernel32.GetCurrentProcess()
        token = ctypes.c_void_p()
        ctypes.windll.advapi32.OpenProcessToken(current_process, 0x20008, ctypes.byref(token))
        admin_sid = ctypes.windll.shell32.IsUserAnAdmin()
        if admin_sid:
            return True
        else:
            return False
    else:
        raise WrongOs('Este Script es solo para Windows')

def checkWinDefender():
    script_str = """
    (Get-MpPreference).DisableRealtimeMonitoring
    """
    output = subprocess.check_output(["powershell", "-Command", script_str], input=None, stderr=subprocess.STDOUT)
    ouputStr = output.decode("utf-8")
    outputBool = not(eval(ouputStr))
    return outputBool

def winVersion():
    script_str = """
    (Get-WmiObject Win32_OperatingSystem).Caption
    """
    output = subprocess.check_output(["powershell", "-Command", script_str], input=None, stderr=subprocess.STDOUT)
    outputStr = output.decode("utf-8")
    return outputStr

def clear():
    os.system ("cls")