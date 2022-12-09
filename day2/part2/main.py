# X is lose, Y is draw, Z is win
# A is rock, B is paper, C is scissors

rps_dict = {
    'A':{
        'X':3, #scissors
        'Y':4, #rock
        'Z':8},#paper
    'B':{
        'X':1, #rock
        'Y':5, #paper
        'Z':9},#scissors
    'C':{
        'X':2, #paper
        'Y':6, #scissors
        'Z':7} #rock
}

# print(sum(list()) for line in open('day2/input.txt').read().line().strip().split(' '))

sum = 0
with open('day2/input.txt') as file:
    for line in file:
        info = line.strip().split(' ')
        result = rps_dict[info[0]][info[1]]
        sum = sum + result

print(sum)