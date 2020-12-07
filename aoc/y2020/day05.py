from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)


sample = [
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL'
]


def convert(seat):
    bin_ = []
    for i in seat:
        if i in 'FL':
            b = '0'
        elif i in 'BR':
            b = '1'
        else:
            print(i)
            raise RuntimeError
        bin_.append(b)
    return ''.join(bin_)[0:7], ''.join(bin_)[7:]


def all_seats():
    ids = []
    for r in range(128):
        for c in range(8):
            ids.append(r * 8 + c)


@timeit
def part1():
    seats = [convert(s) for s in INPUTS]
    ids = [int(s[0], 2) * 8 + int(s[1], 2) for s in seats]

    print(sorted(ids)[-1])
    # 885


@timeit
def part2():
    seats = [convert(s) for s in INPUTS]
    ids = [int(s[0], 2) * 8 + int(s[1], 2) for s in seats]

    every = [r * 8 + c for r in range(128) for c in range(8)]

    dif = set(every) - set(ids)

    print([seat for seat in dif if seat - 1 in ids and seat + 1 in ids])


if __name__ == '__main__':
    part1()
    part2()
