from aoc.day_1 import day_1_func, day_1_p2

def test_day_1():
    input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    assert day_1_func(input) == 24000

def test_day_1_p2():
    input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    assert day_1_p2(input) == 45000
