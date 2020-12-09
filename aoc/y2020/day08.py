from aoc.util import load_inputs_for_source, timeit
import copy

INPUTS = load_inputs_for_source(__file__)


sample = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]


def transform(lines):
    instructions = []
    for line in lines:
        operation = line.split(' ')[0]
        argument = int(line.split(' ')[1])
        instructions.append([False, operation, argument])   # (visited, op, arg)
    return instructions


class Handheld:

    def __init__(self, instructions):
        self.instructions = instructions
        self.potential = copy.deepcopy(instructions)
        self.flipper = 0
        self.counter = 0
        self.accumulator = 0
        self.exit = len(instructions)

    def acc(self, arg):
        self.accumulator += arg
        self.counter += 1

    def jmp(self, arg):
        self.counter += arg

    def nop(self, arg):
        self.counter += 1

    def do(self, instruction):
        visited, operation, argument = instruction

        if not visited:
            instruct = getattr(self, operation)
            instruct(argument)
            instruction[0] = True

        return visited

    def run_repeat(self):
        stop = self.do(self.instructions[0])
        while not stop:
            instruction = self.instructions[self.counter]
            stop = self.do(instruction)

    def run_exit(self):
        while self.counter != self.exit:
            instruction = self.potential[self.counter]
            stop = self.do(instruction)
            if stop:
                self.flip_next()
                self.reset()
                continue

    def flip_next(self):
        self.potential = copy.deepcopy(self.instructions)
        new_op = None
        while not new_op:
            visited, operation, arg = self.potential[self.flipper]
            if operation == 'nop':
                new_op = 'jmp'
            elif operation == 'jmp':
                new_op = 'nop'
            if new_op:
                self.potential[self.flipper][1] = new_op
                self.flipper += 1
                return
            else:
                self.flipper += 1

    def reset(self):
        self.counter = 0
        self.accumulator = 0


@timeit
def part1():
    instructions = transform(INPUTS)

    game = Handheld(instructions)
    game.run_repeat()
    print(game.accumulator)
    # 1671


@timeit
def part2():
    instructions = transform(INPUTS)

    game = Handheld(instructions)
    game.run_exit()
    print(game.accumulator)
    # 892


if __name__ == '__main__':
    part1()
    part2()
