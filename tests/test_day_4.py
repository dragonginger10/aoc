from aoc.day_4 import day_4_p1, day_4_p2

INPUT = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

def test_day_4_p1():
	assert day_4_p1(INPUT) == 2

def test_day_4_p2():
	assert day_4_p2(INPUT) == 4
