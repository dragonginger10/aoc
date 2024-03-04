def day_1_func(input: str) -> int:
    calories: int = 0
    split_lines = input.split("\n")
    calories_list: list[int] = []

    for line in split_lines:
        if line == "":
            calories = 0 
            continue

        calories += int(line) 
        calories_list.append(calories)

    return max(calories_list)

def day_1_p2(input: str) -> int:
    calories: int = 0
    split_lines = input.split("\n")
    calories_list: list[int] = []

    for line in split_lines:
        if line == "":
            calories_list.append(calories)
            calories = 0 
            continue

        calories += int(line) 

    if calories != 0:
        calories_list.append(calories)

    top_3 = sorted(calories_list, reverse=True)[:3]

    return sum(top_3)
