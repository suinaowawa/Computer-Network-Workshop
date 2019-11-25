# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:37:06 2019

@author: Yue
"""
#Code reference:https://medium.com/@makerhacks/python-client-and-server-internet-communication-using-udp-c4f5fc608945

import socket

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print("Oops, something went wrong connecting the socket")
    exit()

while 1:
    message = input("> ")
    if len(message) > 140:
        print("invalid")
        continue
    # encode the message
    message_ = message.encode()
    # send the message
    socket.sendto(message_, ('localhost', 9999))
    # output the response (if any)
    data, ip = socket.recvfrom(1024)
    print("{}: {}".format(ip, data.decode()))
    if message=='exit':        
        socket.close() 
        break
