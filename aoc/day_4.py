def day_4_p1(input: str) -> int:
    data: list[str] = input.splitlines()
    elf_pairs: list[list[str]] = [line.split(",") for line in data]
    contained: int = 0

    for pair in elf_pairs:
        elf1, elf2 = pair
        elf1_numbers = elf_string_to_numbers(elf1)
        elf2_numbers = elf_string_to_numbers(elf2)

        if (elf1_numbers in elf2_numbers) or (elf2_numbers in elf1_numbers):
            contained += 1

    return contained

def elf_string_to_numbers(elf: str) -> str:
    elf_numbers = [int(i) for i in elf.split("-")]
    numbers = [str(i) for i in range(elf_numbers[0], elf_numbers[-1])]
    return "".join(numbers)
