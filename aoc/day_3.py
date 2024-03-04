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

def day_3_p2(input: str) -> int:
	data = input.splitlines()
	sum_priority: int = 0

	for line in range(0,len(data),3):
		bag1 = data[line]
		bag2 = data[line+1]
		bag3 = data[line+2]

		for i in bag1:
			if i in bag2 and i in bag3:
				sum_priority += priority(i)
				break

	return sum_priority


def priority(item: str) -> int:
	for i, l in enumerate(ascii_letters):
		if l == item:
			return i + 1
