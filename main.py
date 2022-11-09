import typer
from src import proc_monitor

app = typer.Typer()

@app.command()
def listen(pid: int):
    proc_monitor.monitor_process_and_system(pid)

if __name__ == "__main__":
    app()