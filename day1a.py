NUMBERS = [str(i) for i in range(10)]

def find2digits(line: str) -> int:
    a, b = '', ''
    for c in line:
        if c in NUMBERS:
            a = c
            break
    for c in line[::-1]:
        if c in NUMBERS:
            b = c
            break
    return int(a+b)


def calculate_calibration_value(text: str) -> int:
    return sum(find2digits(l) for l in text.splitlines())


def test_a():
    text = '''1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet'''
    assert calculate_calibration_value(text) == 142
    

if __name__=='__main__':
    import pathlib
    input = pathlib.Path('inputs/day1a').read_text()
    print(calculate_calibration_value(input))

