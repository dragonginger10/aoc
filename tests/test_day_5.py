from aoc.day_5 import day_5_p1, day_5_p2

INPUT = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

def test_day_5_p1():
    assert day_5_p1(INPUT) == "CMZ"

def test_day_5_p2():
    assert day_5_p2(INPUT) == None
