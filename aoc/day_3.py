from string import ascii_letters
def day_3_p1(input: str) -> int:
	data = input.split("\n")
	sum_priority: int = 0

	for line in data:
		size = len(line)/2
		comp1 = line[:int(size)]
		comp2 = line[int(size):]

		for i in comp1:
			if i in comp2:
				sum_priority += priority(i)
				break

	return sum_priority

def priority(item: str) -> int:
	for i, l in enumerate(ascii_letters):
		if l == item:
			print(i, l)
			return i + 1
