rps_dict = {
    'A':{
        'X':4, 
        'Y':8, 
        'Z':3},
    'B':{
        'X':1, 
        'Y':5, 
        'Z':9},
    'C':{
        'X':7, 
        'Y':2, 
        'Z':6}
}

# print(sum(list()) for line in open('day2/input.txt').read().line().strip().split(' '))

sum = 0
with open('day2/input.txt') as file:
    for line in file:
        info = line.strip().split(' ')
        result = rps_dict[info[0]][info[1]]
        sum = sum + result

print(sum)