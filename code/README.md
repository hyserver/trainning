##文件说明：
- agent.py:执行及打印帮助信息
- Cpu_info.py:监控cpu使用情况
- Loadavg_info.py:监控系统平均负载情况
- Memory_info.py:监控内存使用情况

####执行

python agent.py -h或--help

python agent.py -v  #打印帮助信息

python agent.py -m cpu/memory/all #默认ttl=60

python agent.py -m cpu/memory/all -t value #设置执行周期
