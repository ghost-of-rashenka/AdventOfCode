from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)


sample = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in'
]

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


@timeit
def part1():
    # Cut up the input lines into a batch of passports:
    batch = []
    batches = []
    for line in INPUTS:
        if line:
            batch += line.split(' ')
        else:
            batches.append({b.split(':')[0]: b.split(':')[1] for b in batch})
            batch = []
    batches.append({b.split(':')[0]: b.split(':')[1] for b in batch})
    # Process the number of valid passports:
    valid = []
    for pport in batches:
        pport.pop('cid', None)
        if set(pport.keys()) == req:
            valid.append(pport)
    print(len(valid))
    # 230


@timeit
def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()
