import fileinput

totalTxt = ''.join(list(fileinput.input(files=['Day6/val.txt'])))
arr = [[int(y) for y in x.split(':')[1].split(' ') if y.isnumeric()] for x in totalTxt.split('\n')]

prod = 1

for i in range(len(arr[0])):
    currHoldDown = 1
    while currHoldDown * (arr[0][i] - currHoldDown) <= arr[1][i]: currHoldDown += 1
    prod *= arr[0][i] - currHoldDown - currHoldDown + 1

print(prod)