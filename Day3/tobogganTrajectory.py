with open('input.txt') as f:
    data = f.readlines()
    data = [i.strip() for i in data]

# part 1
print("Part 1")
pos = 0
count = 0
for line in data:
    if line[pos:pos+1:] == '#':
        count += 1
    pos = (pos + 3) % len(line)

print("Nunber of trees: {}".format(count))

# part 2
print("\nPart 2")
trees = 1
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
for slope in slopes:
    pos = 0
    count = 0
    temp = [data[i] for i in range(0,len(data),slope[1])]
    for line in temp:
        if line[pos:pos+1:] == '#':
            count += 1
        pos = (pos + slope[0]) % len(line)

    trees = trees * count

print("Multiplied trees: {}".format(trees))
