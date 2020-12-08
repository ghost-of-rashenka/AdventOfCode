from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)

sample = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]


def organize_rules(rules):
    bags = {}
    for rule in rules:
        split_rule = rule.split(' ')
        bag = ' '.join(split_rule[0:2])
        contents = split_rule[4:]
        if contents[0] == 'no':
            bags.update({bag: []})
        else:
            contains = {}
            i = 0
            while i < len(contents):
                count = contents[i]
                contain = ' '.join(contents[i + 1:i+3])
                contains.update({contain: int(count)})
                i += 4
            bags.update({bag: contains})
    return bags


def found_gold(start_bag, rules):
    if not rules[start_bag]:
        return False
    elif 'shiny gold' in rules[start_bag]:
        return True
    else:
        for other_bag in rules[start_bag]:
            if found_gold(other_bag, rules):
                return True

@timeit
def part1():
    rules = organize_rules(INPUTS)
    golds = 0
    for bag in rules:
        if found_gold(bag, rules):
            golds += 1

    print(golds)
    # 300


@timeit
def part2():
    pass



if __name__ == '__main__':
    part1()
    part2()
