DIGITS: dict[str, str] = {
    s: str(i)
    for i, s in enumerate(
        ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"), 1
    )
}


def find2digits_b(line: str) -> int:
    numbers: list[str] = []
    for i, c in enumerate(line):
        if c in DIGITS.values():
            numbers.append(c)
            continue
        for number, digit in DIGITS.items():
            if line[: i + 1].endswith(number):
                numbers.append(digit)
    return int(numbers[0] + numbers[-1])


def calculate_calibration_value(text: str) -> int:
    return sum(find2digits_b(l) for l in text.splitlines())


TEST = {
    "two1nine": 29,
    "eightwothree": 83,
    "abcone2threexyz": 13,
    "xtwone3four": 24,
    "4nineeightseven2": 42,
    "zoneight234": 14,
    "7pqrstsixteen": 76,
}


def test_find2digits_b():
    for line, number in TEST.items():
        assert find2digits_b(line) == number


def test_b():
    text = "\n".join(TEST.keys())
    assert calculate_calibration_value(text) == 281


if __name__ == "__main__":
    import pathlib

    input = pathlib.Path("inputs/day1").read_text()
    print(calculate_calibration_value(input))
