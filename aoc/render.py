from rich.align import Align
from rich.console import Console
from rich.panel import Panel

console = Console(color_system="truecolor")

def render(p1: type[str|int], p2: type[str|int], day: str) -> None:
    string = f"Part one: [green]{p1}[cyan]\nPart two: [green]{p2}"
    panel = Panel.fit(Align(string, "center"),title=f"Solution for Day {day}")
    console.print(panel, style="cyan")
