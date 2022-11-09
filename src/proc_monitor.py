from traceback import print_tb
import psutil

def monitor_process_and_system(pid: int) -> None:
    if not psutil.pid_exists(pid):
        print("process not found, shutting down")
