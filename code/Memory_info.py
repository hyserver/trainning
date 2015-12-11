#!/usr/bin/env python

# encoding: utf-8
# system memory usage information
# auth:yanghaiying

import psutil

def Memory_info():
    print "####Memory usage####"
    Processes=['total','available','percent','used','free','active','inactive','buffers','cached']
    for i in Processes:
        try:
            print "%s   %s" % (i,getattr(psutil.virtual_memory(),i)) + ' byte'
        except Exception,e:
            print "not exit %s" % i
