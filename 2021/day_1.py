depths = []
increases = 0

with open('day_1.txt', 'r') as file:
    for line in file:
        depths.append(int(line))

for index, value in enumerate(depths):
    if value > depths[index - 1]:
        increases += 1

print(increases)

increases = 0

for index, value in enumerate(depths):
    first_triple = sum(depths[index:index+3])
    second_triple = sum(depths[index + 1: index + 4])
    if second_triple > first_triple:
        increases += 1

print(increases)