from distutils.core import setup
import py2exe


setup(
    options = {
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            "includes":["sip", "sqlite3.dump"],
        }
    },
    windows = [{'script' : 'main.py'}]
    #console = [{'script' : 'main.py'}]
    #'uac_info': "requireAdministrator"}]
)
