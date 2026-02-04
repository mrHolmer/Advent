max_cals = 0
curr_cals = 0
cal_list = []

with open('day_1.txt', 'r') as file:
    for line in file:
        if line != '\n':
            curr_cals += int(line)
        else:
            if curr_cals > max_cals:
                max_cals = curr_cals
            cal_list.append(curr_cals)
            curr_cals = 0
    print(max_cals)
    print(cal_list)
    cal_list.sort(reverse=True)
    print(cal_list)
    print(sum(cal_list[:3]))
