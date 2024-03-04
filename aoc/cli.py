from pathlib import Path

import typer

from aoc.day_1 import day_1_func, day_1_p2
from aoc.day_2 import day_2_p1, day_2_p2
from aoc.render import render
from aoc.utils import file_to_string

app = typer.Typer()

@app.command(name="one")
def day_1(input: Path) -> None:
    data = file_to_string(input)
    answer = day_1_func(data)
    p2_answer = day_1_p2(data)
    render(answer, p2_answer, "one")

@app.command(name="two")
def day_2(input: Path) -> None:
    data = file_to_string(input)
    answer = day_2_p1(data)
    p2_answer = day_2_p2(data)
    render(answer, p2_answer, "two")
