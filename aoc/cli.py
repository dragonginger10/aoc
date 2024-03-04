from pathlib import Path
from typing import Annotated, Optional

import typer
from aocd import get_data

from aoc.day_1 import day_1_func, day_1_p2
from aoc.day_2 import day_2_p1, day_2_p2
from aoc.day_3 import day_3_p1, day_3_p2
from aoc.day_4 import day_4_p1
from aoc.render import render
from aoc.utils import file_to_string

app = typer.Typer()

@app.command(name="one")
def day_1(input: Annotated[
    Optional[Path], 
    typer.Argument(
        help="Optional file for input"
    )
] = None) -> None:
    if input is None:
        data = get_data(day=1, year=2022)
    else:
        data = file_to_string(input)
    answer = day_1_func(data)
    p2_answer = day_1_p2(data)
    render(answer, p2_answer, "one")

@app.command(name="two")
def day_2(input: Annotated[
        Optional[Path],
        typer.Argument(
        help="Optional file for input",
    )
    ] = None) -> None:
    if input:
        data = file_to_string(input)
    else:
        data = get_data(day=2, year=2022)
    answer = day_2_p1(data)
    p2_answer = day_2_p2(data)
    render(answer, p2_answer, "two")

@app.command(name="three")
def day_3(input: Annotated[
        Optional[Path],
        typer.Argument(
        help="Optional file for input",
    )
    ] = None) -> None:
    if input:
        data = file_to_string(input)
    else:
        data = get_data(day=3, year=2022)

    p1 = day_3_p1(data)
    p2 = day_3_p2(data)
    render(p1, p2, "Three")

@app.command(name="four")
def day_4(input: Annotated[
        Optional[Path],
        typer.Argument(
        help="Optional file for input",
    )
    ] = None) -> None:
    if input:
        data = file_to_string(input)
    else:
        data = get_data(day=4, year=2022)

    p1 = day_4_p1(data)
    p2 = None
    render(p1, p2, "Four")
