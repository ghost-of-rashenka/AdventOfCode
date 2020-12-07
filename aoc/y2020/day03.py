from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)


def trees(dx, dy):
    tree_ct = 0
    x, y = 0, 0
    while y < len(INPUTS):
        if INPUTS[y][x] == '#':
            tree_ct += 1

        y += dy
        x = (x + dx) % len(INPUTS[0])

    return tree_ct


@timeit
def part1():
    # 323 tall x 31 wide
    # 323 * 3 = 969 wide
    print(trees(3, 1))
    # 274


@timeit
def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    encounters = [trees(*slope) for slope in slopes]
    prod = 1
    for encounter in encounters:
        prod *= encounter
    print(prod)
    # 6050183040


if __name__ == '__main__':
    part1()
    part2()
