with open('input.txt') as f:
    data = f.readlines()
    data = [pw.strip().split(' ') for pw in data]

# part 1
print("Part 1")
count = 0
for each in data:
    lwr = int(each[0].split('-')[0])
    upr = int(each[0].split('-')[1])
    if lwr <= each[2].count(each[1][0:1:]) <= upr:
        count += 1

print("Number of valid passwords: {}".format(count))


# part 2
print("\nPart 2")
count = 0
for each in data:
    pos1 = int(each[0].split('-')[0])
    pos2 = int(each[0].split('-')[1])
    c = each[1][0:1:]

    if (each[2][pos1-1:pos1] == c) ^ (each[2][pos2-1:pos2] == c):
        count += 1

print("Number of valid passwords: {}".format(count))
