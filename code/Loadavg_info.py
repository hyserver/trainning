#!/usr/bin/env python

# encoding: utf-8
# system loadavg information
# auth:yanghaiying

import os

# Collection system load information
def load_info():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    return loadavg

# Print system load information
def Print_info():
    print "####system loadavg####"
    print "w1_avg",load_info()['lavg_1']
    print "w5_avg",load_info()['lavg_5']
    print "w15_avg",load_info()['lavg_15']
