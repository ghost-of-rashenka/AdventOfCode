import copy
from aoc.util import load_inputs_for_source, timeit
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

INPUTS = load_inputs_for_source(__file__)

joltages = [int(line) for line in INPUTS]


sample1 = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4
]


sample2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3
]


def chain_up(available_adapters, chain):
    adapters = set(available_adapters)
    input_jolts = chain[-1]
    while adapters:
        for jump in range(1, 4):
            adapter = input_jolts + jump
            if adapter in adapters:
                adapters.remove(adapter)
                chain.append(adapter)
                return chain_up(adapters, chain)
    return chain


def count_joltage_differences(chain):
    jumps = {}
    for i in range(1, len(chain)):
        jump = chain[i] - chain[i - 1]
        if jump in jumps:
            jumps[jump] += 1
        else:
            jumps[jump] = 1
    # add the implicit final jump
    if 3 in jumps:
        jumps[3] += 1
    else:
        jumps[3] = 1
    return jumps


def many_chains():
    pass



@timeit
def part1():
    adapters = set(joltages)
    chain = [0]
    chain_up(adapters, chain)
    jumps = count_joltage_differences(chain)
    print(jumps[1] * jumps[3])
    # # 2368
    # print(chain)


@timeit
def part2():
    print(sorted(sample1))

if __name__ == '__main__':
    part1()
    part2()
