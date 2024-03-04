def day_2_p1(input: str) -> int:
	score: int = 0
	scoring = {
		"X": 1,
		"Y": 2,
		"Z": 3,
	}

	data = input.split("\n")

	for line in data:
		if line == "":
			continue
		score += scoring[line[2]]
		if line in ["A Y", "B Z", "C X"]:
			score += 6
		elif line in ["A X", "B Y", "C Z"]:
			score += 3

	return score

def day_2_p2(input: str) -> int:
	score: int = 0
	scoring = {
		"X": 0,
		"Y": 3,
		"Z": 6,
	}

	data = input.split("\n")

	for line in data:
		if line == "":
			continue
		score += scoring[line[2]]

		if line in ["A Y", "B X", "C Z"]:
			score += 1
		elif line in ["A Z", "B Y", "C X"]:
			score += 2
		else:
			score += 3

	return score

