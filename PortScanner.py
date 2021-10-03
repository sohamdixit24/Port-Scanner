#!bin/python3
print("hello,world")
import sys
import socket
from datetime import datetime
 
 #Define your target
if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument!")
    print("Syntax: python3 PortScanner.py <ip>")

#Add a pretty banner
print("-"*50)
print("Scanning target "+target)
print("Time started:"+str(datetime.no()))
print("-"*50)

#Scanning the target
try:
    for port in range(1,65535):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect(target,port)
        if result==0:
            print("Port {} is open",format(port))
        s.close()
except KeyboardInterrupt():
    print("Exiting Program....")
    sys.exit()
except socket.gaierror():
    print("Hostname could not be resolved..")
    sys.exit()
except socket.error:
    print("Couldn't connect to server...")
    sys.exit()


