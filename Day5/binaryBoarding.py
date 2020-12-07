import math

with open('input.txt') as f:
    data = f.readlines()
    data = [i.strip() for i in data]

def find_seat(chars):
    row = int("".join('0' if i == 'F' else '1' for i in chars[:7:]),base=2)
    column = int("".join('0' if i == 'L' else '1' for i in chars[7::]),base=2)
    return row * 8 + column

# part 1
print("Part 1")

seat_nums = []
for seats in data:
    seat_nums.append(find_seat(seats))

print("Highest seat is {}".format(max(seat_nums)))


# part 2
print("\nPart 2")

# for num in sorted(seat_nums):
possible_nums = []
for row in range(128):
    for col in range(8):
        num = (row * 8) + col
        if num not in seat_nums:
            possible_nums.append(num)

for i in range(1, len(possible_nums)-1):
    num = possible_nums[i]
    if (possible_nums[i-1] != num - 1) and (possible_nums[i+1] != num + 1):
        print("My seat is {}".format(num))
        break
