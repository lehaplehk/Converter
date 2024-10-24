# -*- coding: utf-8 -*-
import os
import hashlib
import requests
import json

import subprocess



def serv_restart():
    print("////////Restarting server")
    os.system('pkill -f "server.py"')
    print('::Command "pkill" send')
    os.system('python3 server.py --start &')
    print('::Command "server.py" launch send')


    
if __name__ == "__main__":
    import sys
    if sys.argv[1] == "--restart":
        serv_restart()
    
