#TODO: save data into a csv, read the csv using the other cli function

import psutil
import logging
import time

def save_data_into_csv(data: list) -> str:
    pass

def monitor_process_and_system(pid: int, ttl: int) -> list:
    if not psutil.pid_exists(pid):
        logging.info(f"process with pid {pid} not found")
        return
    
    proc = psutil.Process(pid=pid)

    try:
        while True:
            with proc.oneshot():
                memmory = proc.memory_info().data 
                cpu = proc.cpu_percent(interval=None)
                
                time.sleep(ttl)
    except KeyboardInterrupt:
        logging.info(f"user requested to shutdown, finishing the application")
    except psutil.NoSuchProcess:
        logging.info(f"the process was stopped, finishing the application")