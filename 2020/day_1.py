entries = []

with open('day_1.txt', 'r') as file:
    for line in file:
        entries.append(int(line))

for i in entries:
    for j in entries:
        if i + j == 2020:
            print(i * j)

for i in entries:
    for j in entries:
        for k in entries:
            if i + j + k == 2020:
                print(i * j * k)
