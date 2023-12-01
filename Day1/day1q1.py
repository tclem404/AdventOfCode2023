import fileinput

sum = 0
for line in fileinput.input(files=['Day1/val.txt']):
    line = line.lower()
    nums = [int(i) for i in line if i.isdigit()]
    sum += + 10*nums[0] + nums[-1]

print(sum)