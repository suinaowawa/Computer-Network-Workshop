# -*- coding: utf-8 -*-
"""

This script implements the client application

@author: alpcan
"""

import requests
import json

# import helper data reading functions
from pricetempreader import *
import matplotlib.pyplot as plt

temp_data = import_tempdata()
time_index = 0

def set_point_func(desired_temp,desired_price,temp,price):
    
    set_point = desired_temp - 0.1 * (price - desired_price)
    
    return set_point


price_list = []
temp_list = []
set_point_list = []
#desired_temp = 22
#desired_price = 40
desired_temp = float(input("Please input the desired temperature in °C:"))
desired_price = float(input("Please input the desired price:"))
while True:
    if time_index > 43:
#        time_index = 0
#        continue
        break
    
    # communication basics
    payload = {'time': time_index}
    r = requests.get("http://localhost:8080/price", params=payload)
#r = requests.post("http://localhost:8080/forfun", data=payload)

## If you are behind the university proxy
#proxies = {
#  "http": "http://wwwproxy.unimelb.edu.au:8000",
#  "https": "http://wwwproxy.unimelb.edu.au:8000",
#}

# requests.get("http://www.python.org", proxies=proxies)
## see below for more information
## http://docs.python-requests.org/en/latest/user/advanced/

    # display info on console
    print("Request made: {0} \n".format(r.url))
    print("Response received: {0} ".format(r.text))

#    print(type(r.text))
#    newdict=json.loads(r.text)
    
    price = float(r.text)
    price_list.append(price)
#    print(type(newdict))
    
#    print(newdict['key1'])
    
    current_temp = temp_data[time_index]
    temp_list.append(current_temp)
    
    set_point = set_point_func(desired_temp,desired_price,current_temp,price)
    set_point_list.append(set_point)
    time_index += 1

plt.figure()
plt.plot(temp_list,label='temperature')
plt.plot([desired_temp]*44,label='desired temperature',linestyle='--')
plt.plot(price_list,label='price')
plt.plot(set_point_list,label='temperature set point')
plt.xlabel("time")
plt.ylabel("value")
plt.legend(loc='upper right')
#print("set points",set_point_list)
