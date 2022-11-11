import typer
from src import proc_monitor
import logging
import datetime

app = typer.Typer()

@app.command()
def collect(pid: int, ttl: int):
    logging.basicConfig(
        level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s'
        # ,filename=f"proc-monitoring-{datetime.datetime.now()}.log"       
    )
    collected_data = proc_monitor.monitor_process_and_system(pid, ttl)
    csv_name = proc_monitor.save_data_into_csv(collected_data)

    logging.info(f"collected data saved into {csv_name}")

@app.command()
def view(filename: str):
    pass

if __name__ == "__main__":
    app()