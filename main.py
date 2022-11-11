import typer
from src import proc_monitor
import logging
import datetime

app = typer.Typer()

@app.command()
def listen(pid: int, ttl: int):
    logging.basicConfig(
        level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s',
        filename=f"proc-monitoring-{datetime.datetime.now()}.log"       
    )
    proc_monitor.monitor_process_and_system(pid, ttl)

if __name__ == "__main__":
    app()