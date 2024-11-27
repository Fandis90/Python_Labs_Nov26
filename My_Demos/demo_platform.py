#! /user/bin/env python3
#Description: test which platform you are running on and then get the home path of the user

import sys
import os
import platform

#check on what environemnt we are: windows or other type?
if sys.platform == "win32":
    home = os.environ["HOMEPATH"]
else:
    home = os.environ["HOME"] #this is for linux systems

print("My home directoy is", home)


#information of what hardware and software you are useing by using platform library
print("OS:", platform.system())
print("Service Pack:", platform.platform())
print(platform.machine())
print(platform.architecture())
print(platform.node()) #host name
print(platform.python_implementation()) #type of python we are writting in
#------------------------------------------------

#exit program with return code.
try:
    sys.exit(0) #0 meaninig finished with 0 errors. and (1-255=error code)
except SystemError:
    print("Quitting program...")
    sys.exit(0) #write error code of your choise