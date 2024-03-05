def day_4_p1(input: str) -> int:
    data: list[str] = input.splitlines()
    contained: int = 0

    for line in data:
        elf1, elf2 = [list(map(int, pair.split("-"))) for pair in line.split(",")]
        if elf1[0] != elf2[0]:
            if elf1[0] > elf2[0]:
                inside, outside = elf1, elf2
            else:
                inside, outside = elf2, elf1
        else:
            if elf1[1] < elf2[1]:
                inside, outside = elf1, elf2
            else:
                inside, outside = elf2, elf1
            

        if inside[1] <= outside[1]:
            contained += 1
  
    return contained

def day_4_p2(input: str) -> int:
    data: list[str] = input.splitlines()
    contained: int = 0

    for line in data:
        elf1, elf2 = [list(map(int, pair.split("-"))) for pair in line.split(",")]

        if elf1[0] > elf2[0]: 
            inside, outside = elf1, elf2
        else:
            inside, outside = elf2, elf1

        if inside[0] <= outside[1]:
            contained += 1

    return contained
