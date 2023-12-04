import fileinput

sum = 0
for line in fileinput.input(files=['Day4/val.txt']):
    line = line.replace("\n","")
    line = line.split(":")[1]
    line = line.split("|")
    winningNums = [int(x) for x in line[0].split(' ') if x.isnumeric()]
    numsHave = [int(x) for x in line[1].split(' ') if x.isnumeric()]
    count = len([x for x in numsHave if x in winningNums])

    if count > 0:
        sum += 2**(count-1)

print(sum)