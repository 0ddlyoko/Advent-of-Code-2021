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


def compute(vals):
    # https://adventofcode.com/2021/day/3
    if len(vals) == 0:
        return 0
    # We just need to calculate the gamma rate as the epsilon rate is
    # equals to all bits to 1 - gamma rate

    # Size of the array
    ln = len(vals)
    # Length of an entry
    entry_size = len(vals[0])

    # Generate the table
    tab = [0] * entry_size
    for entry in vals:
        for i in range(0, entry_size):
            tab[i] += int(entry[i])
    # If an entry of the table is > ln / 2, the most common bit is 1
    final_table = [1 if (x > ln / 2) else 0 for x in tab]
    # Transform it to decimal
    gamma = int("".join([str(x) for x in final_table]), 2)
    # Find the top number (all bit to 1)
    top_number = 2**entry_size - 1
    # Now that we have gamma, we can easily calculate epsilon
    epsilon = top_number - gamma

    return gamma * epsilon


if __name__ == "__main__":
    ints = read_values()
    print(compute(ints))
