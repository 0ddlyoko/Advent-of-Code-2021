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
    # https://adventofcode.com/2021/day/1#part2
    if len(vals) == 0:
        return 0
    result = 0
    for i in range(0, len(vals) - 3):
        old = sum(vals[i:i+3])
        new = sum(vals[i + 1:i + 4])
        if new > old:
            result += 1
    return result


if __name__ == "__main__":
    ints = read_values()
    print(compute(ints))
