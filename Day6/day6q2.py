import fileinput

totalTxt = ''.join(list(fileinput.input(files=['Day6/val.txt'])))
arr = [[(y) for y in x.split(':')[1].split(' ') if y.isnumeric()] for x in totalTxt.split('\n')]
arr = [int(''.join(x)) for x in arr]
prod = 1

prod = 1
currHoldDown = 1
while currHoldDown * (arr[0] - currHoldDown) <= arr[1]: currHoldDown += 1
prod *= arr[0] - currHoldDown - currHoldDown + 1

print(prod)