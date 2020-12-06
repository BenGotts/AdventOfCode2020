import re

def get_input():
    with open('input.txt') as f:
        data = []
        passport = []
        for line in f:
            if line != '\n':
                passport.extend(line.strip().split(' '))
            else:
                data.append(passport)
                passport = []

    return data

def check_valid(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid is optional
    in_passport = [False, False, False, False, False, False, False]

    for field in passport:
        if field[:3:] in required:
            in_passport[required.index(field[:3:])] = True

    return all(in_passport)

def check_valid_extra(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid is optional
    in_passport = [False, False, False, False, False, False, False]

    for field in passport:
        if field[:3:] in required:
            idx = required.index(field[:3:])
            switch = {
            0: True if re.match("^(19[2-9][0-9]|200[0-2])$", field[4::]) else False,
            1: True if re.match("^(20(1[0-9]|20))$", field[4::]) else False,
            2: True if re.match("^(20(2[0-9]|30))$", field[4::]) else False,
            3: True if re.match("^((1([5-8][0-9]|9[0-3])cm)|((59|[6][0-9]|7[0-6])in))$", field[4::]) else False,
            4: True if re.match("^#[0-9a-f]{6}$", field[4::]) else False,
            5: True if field[4::] in ['amb','blu','brn','gry','grn','hzl','oth'] else False,
            6: True if re.match("^[0-9]{9}$", field[4::]) else False
            }
            in_passport[idx] = switch.get(idx, False)
    return all(in_passport)

# part 1
print("Part 1")
data = get_input()

count = 0
for passport in data:
    if check_valid(passport):
        count += 1

print("{} valid passports".format(count))


# part 1
print("\nPart 2")
data = get_input()

count = 0
for passport in data:
    if check_valid_extra(passport):
        count += 1

print("{} valid passports".format(count))
