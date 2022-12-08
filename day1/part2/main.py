sum=0
groups=[]

with open("day1/input.txt", "r") as f:
    for line in f: 
        if len(line) > 1:
            sum = sum + int(line)
        else:
            groups.append(sum)
            sum = 0

first = second = third = -1

for i in range(len(groups)):
    if (groups[i] > first):
        third = second
        second = first
        first = groups[i]
    elif (groups[i] > second and groups[i] != first):
        third = second
        second = groups[i]
    elif (groups[i] > third and groups[i] != second):
        third = groups[i]

print(first + second + third)