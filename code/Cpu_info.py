#!/usr/bin/env python

# encoding: utf-8
# system cpu information
# auth:yanghaiying

import psutil

def Cpu_info():
    print "####CPU usage####"
    Processes=['user','nice','system','idle','iowait','irq','softirq','steal','guest','guest_nice']
    for i in Processes:
        try:
            print "%s   %s" % (i,getattr(psutil.cpu_times(),i))
        except Exception,e:
            print "not exit %s" % i
