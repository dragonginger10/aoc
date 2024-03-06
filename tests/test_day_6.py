from aoc.day_6 import day_6_func

TEST_1 = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
    "nppdvjthqldpwncqszvftbrmjlhg": 6,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11,
}

TEST_2 = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
    "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
    "nppdvjthqldpwncqszvftbrmjlhg": 23,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26,
}

def test_day_6_p1():
    for k, v in TEST_1.items():
        assert day_6_func(k, 4) == v

def test_day_6_p2():
    for k, v in TEST_2.items():
        assert day_6_func(k, 14) == v
