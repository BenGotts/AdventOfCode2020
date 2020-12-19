with open('input.txt') as f:
    # stream = open("input.txt")
    lines = f.readlines()
    bagDictionary = dict()

    for line in lines:
        line = line.strip(".\n").replace('bags', 'bag').split(' contain ')
        bagDictionary[line[0]] = line[1].split(", ")


# part 1
print('Part 1')

def findSubBag(bag, name='shiny gold bag'):
    found = False
    for subBag in bagDictionary[bag]:
        if subBag != 'no other bag':
            if (subBag.split(' ', 1)[1] == name) or (findSubBag(subBag.split(' ', 1)[1])):
                found = True
    return found

tot = 0
for bag in bagDictionary:
    if findSubBag(bag):
        tot += 1
        
print(tot)

# part 2
print('\nPart 2')

def iterateAllBagsInBag(bag='shiny gold bag'):
    tot = 0
    for subBag in bagDictionary[bag]:
        if subBag != 'no other bag':
            parentCount = int(subBag.split(' ', 1)[0])
            tot = tot + parentCount

            childCount = parentCount * iterateAllBagsInBag(subBag.split(' ', 1)[1])
            tot = tot + childCount
    return tot

print(iterateAllBagsInBag())