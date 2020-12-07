from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)

sample = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b'
]


def process_groups(raw_imput):
    groups = []
    answers = []
    for line in raw_imput:
        if line:
            answers.append(line)
        else:
            groups.append(answers)
            answers = []
    groups.append(answers)
    return groups


@timeit
def part1():
    groups = process_groups(INPUTS)

    all_ = []
    for group in groups:
        questions = ''
        for traveller in group:
            for answer in traveller:
                if answer not in questions:
                    questions += answer
        all_.append(questions)

    print(sum([len(q) for q in all_]))
    # 6930


@timeit
def part2():
    groups = process_groups(INPUTS)
    all_ = []
    for group in groups:
        questions = {}
        for traveller in group:
            for answer in traveller:
                if answer not in questions:
                    questions[answer] = 1
                else:
                    questions[answer] += 1

        common = []
        for q in questions:
            if questions[q] == len(group):
                common.append(q)
        all_.append(common)
    print(sum([len(q) for q in all_]))
    # 3585


if __name__ == '__main__':
    part1()
    part2()
