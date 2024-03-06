from rich import print
N = 9
LINES = 8

def day_5_p1(input: str) -> str:
	answer: str = ""
	stacks, moves = create_stacks(input)
	for line in moves.splitlines():
		token = line.split(" ")
		n, src, dst = map(int, [token[1], token[3], token[5]])
		src -= 1
		dst -= 1

		for _ in range(n):
			pop = stacks[src].pop()
			stacks[dst].append(pop)

	for s in stacks:
		answer += s[-1]

	return answer

def day_5_p2(input: str) -> str:
	answer: str = ""
	stacks, moves = create_stacks(input)
	for line in moves.splitlines():
		token = line.split(" ")
		n, src, dst = map(int, [token[1], token[3], token[5]])
		src -= 1
		dst -= 1

		pop = stacks[src][-n:]
		del stacks[src][-n:]
		stacks[dst] += pop

	for s in stacks:
		answer += s[-1]

	return answer

def create_stacks(input: str) -> (list[str], list[str]):
	parts, moves = input.split("\n\n")
	drawing = parts.splitlines()
	num_stacks = [int(i) for i in drawing[-1] if i != ' ']
	n = max(num_stacks)
	stacks = [[] for _ in range(n)]
	
	for line in drawing[:-1]:
		crates = line[1::4]
		for j, c in enumerate(crates):
			if c != " ":
				stacks[j].append(c)

	return [stack[::-1] for stack in stacks], moves
	
