freq = 0
status = 0
changes = []
stati = []

with open('day_1.txt', 'r') as file:
    for line in file:
        changes.append(int(line))

print(changes)


def add_stati(list):
    global status
    for i in list:
        status += i
        stati.append(status)

add_stati(changes)

while len(set(stati)) == len(stati):
    add_stati(changes)

print(stati)



def first(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]

print(first(stati))
