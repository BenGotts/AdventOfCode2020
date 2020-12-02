with open('input.txt') as f:
    data = f.readlines()
    data = [int(num.strip()) for num in data]

# part 1
print("Part 1")
for i in range(len(data)):
    for j in range(i, len(data)):
        if i != j and data[i] + data[j] == 2020:
            print("{} + {} = 2020".format(data[i], data[j]))
            print("{} * {} = {}".format(data[i], data[j], data[i] * data[j]))


# part 2
print("\nPart 2")
for i in range(len(data)):
    for j in range(i, len(data)):
        if i != j:
            for k in range(j, len(data)):
                if j != k and data[i] + data[j] + data[k] == 2020:
                    print("{} + {} + {} = 2020".format(data[i], data[j], data[k]))
                    print("{} * {} * {} = {}".format(data[i], data[j], data[k], data[i] * data[j] * data[k]))
