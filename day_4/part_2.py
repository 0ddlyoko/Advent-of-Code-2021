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


def read_line(line):
    return [[int(x), False] for x in line.split(" ") if bool(x)]


def get_table(vals):
    tables = []
    # Skip first
    for i in range(0, int((len(vals) - 1) / 6)):
        # Skip empty line
        tables.append([[
            read_line(vals[i * 6 + 2]),
            read_line(vals[i * 6 + 3]),
            read_line(vals[i * 6 + 4]),
            read_line(vals[i * 6 + 5]),
            read_line(vals[i * 6 + 6]),
        ], False])
    return tables


def sum_unmarked(bingo):
    result = 0
    for row in bingo:
        for cell in row:
            if not cell[1]:
                result += cell[0]
    return result


def check_bingo(bingo, nbr):
    for row_number, row in enumerate(bingo):
        for col_number, cell in enumerate(row):
            if cell[0] == nbr and not cell[1]:
                cell[1] = True
                # Check if win
                # Check row
                if all([rec[1] for rec in row]):
                    return True
                # Check col
                col = [rec[col_number] for rec in bingo]
                if all([rec[1] for rec in col]):
                    return True
                break
        else:
            continue
        break
    return False


def compute(vals):
    # https://adventofcode.com/2021/day/4#part2
    if len(vals) == 0:
        return 0
    numbers = [int(x) for x in vals[0].split(",")]
    # First, fill the table with bingo
    table = get_table(vals)
    result = 0
    rest = len(table)
    for nbr in numbers:
        for bingo in table:
            if not bingo[1] and check_bingo(bingo[0], nbr):
                rest -= 1
                bingo[1] = True
                if rest == 0:
                    # It was the last bingo !
                    result = sum_unmarked(bingo[0]) * nbr
                    break
        else:
            continue
        break
    return result


if __name__ == "__main__":
    data = read_values()
    print(compute(data))
