import ctypes
import os

class WrongOs(Exception):
    def __init__(self, message):
        self.message = message

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
    import subprocess
    script_str = """
    (Get-MpPreference).DisableRealtimeMonitoring
    """
    output = subprocess.check_output(["powershell", "-Command", script_str], input=None, stderr=subprocess.STDOUT)
    return output.decode("utf-8")
