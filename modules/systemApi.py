import ctypes
import os
import subprocess
from modules.errors import WrongOs
from modules.colorsLog import *

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

def active(key):
    try:
        log('Borrando clave actual...')
        subprocess.call('slmgr.vbs -upk', shell=True)

        greenlog('Instalando clave de producto...')
        script_str = 'slmgr /ipk ' + key
        subprocess.call(script_str, shell=True)

        log('Estableciendo conección con el servidor KMS (kms.digiboy.ir)...')
        subprocess.call('slmgr /skms kms.digiboy.ir', shell=True)

        log('Activando windows con clave y servidor KMS...')
        subprocess.call('slmgr /ato', shell=True)
        return True
    except:
        return False
        
def executeCmdCommandExternal(command):
    subprocess.call(f'start cmd.exe @cmd /k "{command}"', shell=True)

def executeCmdCommand(command):
    subprocess.call(command, shell=True)

def enabledGpedit():
    executeCmdCommandExternal('start gpedit-enabler.bat')

def clear():
    os.system ("cls")