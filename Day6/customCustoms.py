# part 1
print("Part 1")

with open('input.txt') as f:
    answers = [set(q.replace('\n', '')) for q in f.read().split('\n\n')]

print("The sum is {}".format(sum([len(q) for q in answers])))

# part 2
print("\nPart 2")

with open('input.txt') as f:
    groups = []
    temp = []
    for line in f.read().split('\n'):
        if line != '':
            temp.append(line)
        else:
            groups.append(temp)
            temp = []

tot = 0
for i, group in enumerate(groups):
    for ans in answers[i]:
        if all([ans in g for g in group]):
            tot += 1

print("{} groups".format(tot))