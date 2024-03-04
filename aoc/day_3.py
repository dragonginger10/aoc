from string import ascii_letters
def day_3_p1(input: str) -> int:
	data = input.splitlines()
	sum_priority: int = 0

	for line in data:
		size = len(line)/2
		comp1 = line[:size]
		comp2 = line[size:]

		for i in comp1:
			if i in comp2:
				sum_priority += priority(i)

	return sum_priority

def priority(item: str) -> int:
	for i, l in range(ascii_letters):
		if l == item:
			return i + 1
