from aoc.util import load_inputs_for_source, timeit

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
        self.potential = self.instructions.copy()
        self.flip = 0
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

    def run(self):
        print(self.instructions)
        stop = self.do(self.instructions[0])
        while not stop:
            instruction = self.instructions[self.counter]
            print(instruction)
            stop = self.do(instruction)
        print(self.accumulator)
        self.reset()

    def run2(self):
        pass

    def flip_next(self):
        self.potential = self.instructions.copy()
        self.flip += 1
        while True:
            instruction = self.potential[self.flip][1]
            if instruction == 'nop':
                self.potential[self.flip][1] = 'jmp'
                break
            elif instruction == 'jmp':
                self.potential[self.flip][1] = 'nop'
                break
            self.flip += 1

    def reset(self):
        self.counter = 0
        self.accumulator = 0


@timeit
def part1():
    instructions = transform(sample)

    game = Handheld(instructions)
    game.run()


@timeit
def part2():
    instructions = transform(sample)
    game = Handheld(instructions)
    print(game.potential)
    game.flip_next()
    print(game.potential)
    game.flip_next()
    print(game.potential)
    game.flip_next()
    print(game.potential)


if __name__ == '__main__':
    part1()
    part2()
