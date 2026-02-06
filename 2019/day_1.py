def get_fuel(line):
    return int(line / 3) - 2

sum = 0

with open('day_1.txt', 'r') as file:
    for line in file:
        sum += (get_fuel(int(line)))

print(sum)

def recursive_fuel(line):
    fuel = get_fuel(line)
    if fuel <= 0:
        return 0
    return fuel + recursive_fuel(fuel)

sum = 0

with open('day_1.txt', 'r') as file:
    for line in file:
        sum += (recursive_fuel(int(line)))

print(sum)