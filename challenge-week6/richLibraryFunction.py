from rich.console import Console
from rich.progress import track
import time

console = Console()

def loading_simulation():
    console.print("[bold cyan]Creating README...[/bold cyan]")
    for _ in track(range(10), description="Finalizing..."):
        time.sleep(0.2)
    console.print("[bold green]README Created Successfully[/bold green]")