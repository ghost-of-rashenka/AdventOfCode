import itertools
from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)


@timeit
def part1():
    numbers = [int(i) for i in INPUTS]

    print({i[0] * i[1] for i in itertools.combinations(numbers, 2) if i[0] + i[1] == 2020})
    # 440979


@timeit
def part2():
    numbers = [int(i) for i in INPUTS]

    print({i[0] * i[1] * i[2] for i in itertools.combinations(numbers, 3) if i[0] + i[1] + i[2] == 2020})
    # 82498112


if __name__ == '__main__':
    part1()
    part2()
