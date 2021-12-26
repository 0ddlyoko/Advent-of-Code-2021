def read_values():
    lst = []
    try:
        while True:
            nbr = int(input(""))
            lst.append(nbr)
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
    ints = read_values()
    print(compute(ints))
