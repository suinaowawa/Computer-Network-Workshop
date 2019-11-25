# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:36:20 2019

@author: Yue
"""

import socket
import time

# set up the socket using local address
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('localhost', 9999))
while 1:   
    # get the data sent to us
    data, ip = socket.recvfrom(1024)
    # display
    print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))    
    # send acknowledge with timestamp back
    now = int(round(time.time()*1000))
    now02 = time.strftime('%Y-%m-%d %H:%M:%S ack',time.localtime(now/1000))
    socket.sendto(now02.encode(), ip)
    if data.decode()=='exit':
        socket.shutdown(0)
        socket.close()
        break