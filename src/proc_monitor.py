#TODO: save data into a csv, read the csv using the other cli function

import psutil
import logging
import time
import datetime
import csv

def save_data_into_csv(data: list) -> str:
    header = ['timestamp', 'memmory', 'cpu', 'write_bytes', 'read_bytes']

    filename = f'collected-data-{datetime.datetime.now()}.csv'

    with open(filename, 'w') as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(data)

        file.close()

    return filename


def monitor_process_and_system(pid: int, ttl: int) -> list:
    collected_data = []

    if not psutil.pid_exists(pid):
        logging.info(f"process with pid {pid} not found")
        return None
    
    proc = psutil.Process(pid=pid)

    try:
        while True:
            with proc.oneshot():
                memmory = proc.memory_info().data 
                cpu = proc.cpu_percent(interval=None)
                wrote = proc.io_counters().write_bytes
                read = proc.io_counters().read_bytes
                timestamp = datetime.datetime.timestamp(datetime.datetime.now())
                
                new_data = [
                    timestamp,
                    memmory,
                    cpu,
                    wrote,
                    read
                ]

                collected_data.append(new_data)

                logging.info(f"collecting {new_data}")
                
                time.sleep(ttl)
    except KeyboardInterrupt:
        logging.info(f"user requested to shutdown, finishing the application")
        return collected_data
    except psutil.NoSuchProcess:
        logging.info(f"the process was stopped, finishing the application")
        return collected_data
