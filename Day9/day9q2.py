import fileinput

lists = [[int(y) for y in x.split(' ')] for x in list(fileinput.input(files=['Day9/val.txt']))]

total = 0
for x in lists:
    currList = []
    for i in range(len(x) - 1): currList.append(x[i+1] - x[i])
    beginVals = [currList[0]]
    while currList != [0]*len(currList):
        nextList = []
        for i in range(len(currList) - 1): nextList.append(currList[i+1] - currList[i])
        currList = nextList
        beginVals.append(currList[0])

    smallTotal = 0
    for i in range(len(beginVals) - 1, -1,-1):
        smallTotal = beginVals[i] - smallTotal
    total += -1 * smallTotal + x[0]

print(total)
