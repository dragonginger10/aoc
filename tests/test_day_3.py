from aoc.day_3 import day_3_p1, day_3_p2

INPUT = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

def test_day_3_p1():
    assert day_3_p1(INPUT) == 157

def test_day_3_p2():
    assert day_3_p2(INPUT) == 70
