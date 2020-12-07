from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)


def transform(inputs):
    transformed = []
    for line in inputs:
        policy, password = line.split(':')
        char = policy[-1]
        pt1, pt2 = policy[0:-2].split('-')
        transformed.append((char, int(pt1), int(pt2), password.strip()))
    return transformed


@timeit
def part1():

    transformed = transform(INPUTS)

    valid = [pw[3] for pw in transformed if pw[1] <= pw[3].count(pw[0]) <= pw[2]]
    print(len(valid))
    # 456


@timeit
def part2():
    transformed = transform(INPUTS)

    valid = [p[3] for p in transformed
             if (p[3][p[1] - 1] == p[0] or p[3][p[2] - 1] == p[0])
             and not p[3][p[1] - 1] == p[3][p[2] - 1]]
    print(len(valid))
    # 308


if __name__ == '__main__':
    part1()
    part2()
