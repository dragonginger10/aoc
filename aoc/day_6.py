def day_6_func(input: str, length: int) -> int:
    test: list[str] = [c for c in input[0:length-1]]
    answer: int = length

    for char in input[length-1:]:
        test.append(char)
        counts = {c:test.count(c) for c in test}
        if len(counts) == length:
            break
        answer += 1
        del test[0]

        
    return answer
