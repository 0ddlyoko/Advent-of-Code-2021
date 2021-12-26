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


def calc(table, less_bit):
    idx = 0
    ln = len(table)
    while len(table) > 1 and idx < ln:
        # First, count the number of 1 in the {idx}th digit
        nbr = 0
        for x in table:
            nbr += int(x[idx])
        # Check which bit is dominant
        bit = int(nbr >= len(table) / 2)
        if less_bit:
            bit = not bool(bit)
        # Filter
        table = [val for val in table if int(val[idx]) == bit]
        idx += 1
    return table[0]


def compute(vals):
    # https://adventofcode.com/2021/day/3#part2
    if len(vals) == 0:
        return 0

    o2 = int(calc(vals, True), 2)
    co2 = int(calc(vals, False), 2)

    return o2 * co2


if __name__ == "__main__":
    ints = read_values()
    print(compute(ints))
