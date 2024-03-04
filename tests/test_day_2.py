from aoc.day_2 import day_2_p1, day_2_p2

def test_day_2():
    input = "A Y\nB X\nC Z"
    assert day_2_p1(input) == 15

def test_day_2_p2():
    input = "A Y\nB X\nC Z"
    assert day_2_p2(input) == 12
