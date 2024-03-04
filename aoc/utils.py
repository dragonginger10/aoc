from pathlib import Path


def file_to_string(input: Path) -> str:
    with open(input) as f:
        data = f.read()

    return data
