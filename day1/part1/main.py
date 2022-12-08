sum=0
groups=[]

with open("day1/input.txt", "r") as f:
    for line in f: 
        if len(line) > 1:
            sum = sum + int(line)
        else:
            groups.append(sum)
            sum = 0

print(max(groups))
print(groups.index(max(groups)))