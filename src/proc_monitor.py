from traceback import print_tb
import psutil
import logging
import time

def monitor_process_and_system(pid: int, ttl: int) -> None:
    if not psutil.pid_exists(pid):
        logging.info(f"process with pid {pid} not found")
    
    proc = psutil.Process(pid=pid)

    try:
        while True:
            with proc.oneshot():
                memmory = proc.memory_info().data 
                cpu = proc.cpu_percent(interval=None)
                
                print(f"MEM = {memmory}, CPU = {round(cpu,2)}%")

                time.sleep(ttl)
    except KeyboardInterrupt:
        logging.info(f"user requested to shutdown, finishing the application")
    except psutil.NoSuchProcess:
        logging.info(f"the process was stopped, finishing the application")