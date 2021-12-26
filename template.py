def read_values():
    lst = []
    inp = input("")
    try:
        while inp.lower() != "eof":
            lst.append(inp)
            inp = input("")
    except ValueError:
        # End of the input
        pass
    return lst


def compute(vals):
    # https://adventofcode.com/2021/day/
    if len(vals) == 0:
        return 0
    result = 0
    return result


if __name__ == "__main__":
    data = read_values()
    print(compute(data))
