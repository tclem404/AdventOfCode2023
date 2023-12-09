import fileinput

lists = [[int(y) for y in x.split(' ')] for x in list(fileinput.input(files=['Day9/val.txt']))]

total = 0
for x in lists:
    currList = []
    for i in range(len(x) - 1): currList.append(x[i+1] - x[i])
    endVals = [currList[-1]]
    while currList != [0]*len(currList):
        nextList = []
        for i in range(len(currList) - 1): nextList.append(currList[i+1] - currList[i])
        currList = nextList
        endVals.append(currList[-1])

    total += sum(endVals) + x[-1]

print(total)
