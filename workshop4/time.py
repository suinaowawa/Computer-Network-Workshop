# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:33:54 2019

@author: Yue
"""
import datetime
def format_time(seconds):
    if seconds < 400:
        s = float(seconds)
        return "%.1f seconds" % (s,)
    elif seconds < 4000:
        m = seconds / 60.0
        return "%.2f minutes" % (m,)
    else:
        h = seconds / 3600.0
        return "%.2f hours" % (h,)
now = datetime.datetime.now()

#start = now.replace(hour)
start = now.replace(hour=0,minute=0,second=0,microsecond=0)
total_second = (now-start).total_seconds()
print(total_second)
total_minute = total_second / 60
print(total_minute)
time_index = total_minute // 30
print(time_index)
def calcu_time_index():
    start = now.replace(hour=0,minute=0,second=0,microsecond=0)
    total_second = (now-start).total_seconds()
#    print(total_second)
    total_minute = total_second / 60
#    print(total_minute)
    time_index = total_minute // 30
#    print(time_index)
    return time_index
    
#now = datetime.time()
#print(now)
#    # the time stamp of now
#
#    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
#    # the time stamp of 00:00:00 on the same day
#
#    minutes = (now - midnight).seconds / 60
#    # how many minutes since midnight
#
#    #time_index = minutes / 30
#    time_index = minutes*60
#    # divide 24*60 minutes into 48 slots (30 min / slot)
#
#    return time_index