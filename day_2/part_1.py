def read_values():
    lst = []
    inp = input("")
    try:
        while inp != "":
            lst.append(inp)
            inp = input("")
    except ValueError:
        # End of the input
        pass
    return lst


# horizontal, depth
instructions = {
    'forward': [1, 0],
    'down': [0, 1],
    'up': [0, -1],
}


def compute(vals):
    # https://adventofcode.com/2021/day/2
    if len(vals) == 0:
        return 0
    total = [0, 0]
    for val in vals:
        inst, nbr = val.split()
        total = [x + (y * int(nbr)) for x, y in zip(total, instructions[inst])]

    return total[0] * total[1]


if __name__ == "__main__":
    ints = read_values()
    print(compute(ints))
