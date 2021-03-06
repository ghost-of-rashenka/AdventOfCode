from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)

integers = [int(i) for i in INPUTS]

sample = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]


class XmasParser:

    def __init__(self, preamble_size=5, inputs=None):
        self.numbers = tuple(inputs)
        self.head = preamble_size
        self.tail = 0

    @property
    def window(self):
        return tuple(self.numbers[self.tail:self.head])

    @property
    def next(self):
        return self.numbers[self.head]

    def move(self, jump=1):
        num = self.numbers[self.head]
        self.tail += jump
        self.head += jump
        if self. head >= len(self.numbers):
            raise IndexError('End of XMAS stream')
        return num

    def is_valid(self, number):
        available = list(self.window)
        for n in self.window:
            available.remove(n)
            if (number - n) in available:
                return True
        return False

    def find_invalid(self):
        while self.is_valid(self.next):
            self.move()
        return self.next

    def crack(self):
        invalid = self.find_invalid()
        contiguous = []
        start = 0
        i = 0
        while True:
            contiguous.append(self.numbers[start + i])
            if sum(contiguous) == invalid:
                break
            elif sum(contiguous) > invalid:
                start += 1
                i = 0
                contiguous = []
            else:
                i += 1

        return max(contiguous) + min(contiguous)


@timeit
def part1():
    x = XmasParser(25, integers)
    print(x.find_invalid())
    # 36845998


@timeit
def part2():
    x = XmasParser(25, integers)
    weakness = x.crack()
    print(weakness)
    # 4830226


if __name__ == '__main__':
    part1()
    part2()
