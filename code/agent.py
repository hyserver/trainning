#!/usr/bin/env python

# encoding: utf-8
# system agent information collection
# auth:yanghaiying

import sys
import time
import Loadavg_info
import Cpu_info
import Memory_info

# print help information
def help():
    print '''
    Usage: python agent.py [Options]

    Options:

    -v, --version show program version number and exit
    -h, --help show this help message and exit
    -t, --ttl set agent period, default is 60s
    -m MODULE, --module=MODULE
    use module MODULE

    Modules:
        all, cpu, memory
    '''
def run(ttl=60):
    if 2 > len(sys.argv):
        help()
    else:
        if sys.argv[1]==str('-v'):
            print "agent v0.1"
        elif sys.argv[1]==str('-h') or sys.argv[1]==str('--help'):
            help()
        elif sys.argv[1]==str('-m') and sys.argv[2]=='all':
            while ttl > 0:
                Loadavg_info.Print_info()
                Cpu_info.Cpu_info()
                Memory_info.Memory_info()
                time.sleep(1)
                ttl = ttl - 1

        elif sys.argv[1] == str('-m') and sys.argv[2]=='loadavg':
            while ttl > 0:
                Loadavg_info.Print_info()
                time.sleep(1)
                ttl = ttl - 1

        elif sys.argv[1] == str('-m') and sys.argv[2] == 'cpu':
            while ttl > 0:
                Cpu_info.Cpu_info()
                time.sleep(1)
                ttl = ttl - 1

        elif sys.argv[1]==str('-m') and sys.argv[2]=='memory':
            while ttl > 0:
                Memory_info.Memory_info()
                time.sleep(1)
                ttl = ttl - 1

if 4 > len(sys.argv):
    run()
elif sys.argv[3]==str('-t') and sys.argv[4] > 0:
    run(int(sys.argv[4]))
else:
    help()
