from aoc.util import load_inputs_for_source, timeit

INPUTS = load_inputs_for_source(__file__)


sample = [
    'eyr:1972 cid:100'
    'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
    '',
    'iyr:2019',
    'hcl:#602927 eyr:1967 hgt:170cm',
    'ecl:grn pid:012533040 byr:1946',
    '',
    'hcl:dab227 iyr:2012'
    'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
    '',
    'hgt:59cm ecl:zzz',
    'eyr:2038 hcl:74454a iyr:2023',
    'pid:3556412378 byr:2007',
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
    'hcl:#623a2f',
    '',
    'eyr:2029 ecl:blu cid:129 byr:1989',
    'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
    '',
    'hcl:#888785',
    'hgt:164cm byr:2001 iyr:2015 cid:88',
    'pid:545766238 ecl:hzl',
    'eyr:2022',
    '',
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
]

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def process_batch(raw_batch):
    batch = []
    batches = []
    for line in raw_batch:
        if line:
            batch += line.split(' ')
        else:
            batches.append({b.split(':')[0]: b.split(':')[1] for b in batch})
            batch = []
    batches.append({b.split(':')[0]: b.split(':')[1] for b in batch})
    return batches


@timeit
def part1():
    # Cut up the input lines into a batch of passports:
    passports = process_batch(INPUTS)
    # Process the number of valid passports:
    valid = []
    for pport in passports:
        pport.pop('cid', None)
        if set(pport.keys()) == req:
            valid.append(pport)
    print(len(valid))
    # 230


def validate(pport):
    valid_hcl = '0123456789abcdef'
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    try:
        if len(pport['byr']) != 4:
            return False
        if not 1920 <= int(pport['byr']) <= 2002:
            return False
        if len(pport['iyr']) != 4:
            return False
        if not 2010 <= int(pport['iyr']) <= 2020:
            return False
        if len(pport['eyr']) != 4:
            return False
        if not 2020 <= int(pport['eyr']) <= 2030:
            return False
        if not pport['hcl'][0] == '#':
            return False
        if len([c for c in pport['hcl'][1:] if c in valid_hcl]) != 6:
            return False
        if pport['ecl'] not in valid_ecl:
            return False
        if len([d for d in pport['pid'] if d.isdigit()]) != 9:
            return False
        # Height is most complicated:
        unit = pport['hgt'][-2:]
        measure = int(pport['hgt'][0:-2])
        if unit == 'cm':
            if not 150 <= measure <= 193:
                return False
        elif unit == 'in':
            if not 59 <= measure <= 76:
                return False
        else:
            return False
    except KeyError:
        return False
    except ValueError:
        return False
    return True


@timeit
def part2():
    passports = process_batch(INPUTS)

    valid = [p for p in passports if validate(p)]
    print(len(valid))
    # 156


if __name__ == '__main__':
    part1()
    part2()
