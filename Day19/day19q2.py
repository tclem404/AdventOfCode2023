import fileinput

instructions = [x.replace('\n', '') for x in list(fileinput.input(files=['Day19/val.txt']))]

partialDict = instructions[0:instructions.index('')]

for i, obj in enumerate(partialDict):
    partialDict[i] = '\"' + obj[0:obj.index('{')] + '\":' + str(obj[obj.index('{') + 1: -1].split(','))

dictionary = eval('{' + ','.join(partialDict) + '}')

def decisionTree(key, step, currRanges):
    if key == 'A':
        total = 1
        for range in currRanges:
            total *= 1 + range[1] - range[0]
        return total
    if key == 'R':
        return 0

    insuction = dictionary[key][step]

    if step == len(dictionary[key]) - 1: return decisionTree(insuction, 0, currRanges)

    val = 0
    match insuction[0]:
        case 'x': val = 0
        case 'm': val = 1
        case 'a': val = 2
        case 's': val = 3
    gt = insuction[1] == '>'
    newVal = int(insuction[2:insuction.index(':')])
    returnTotal = 0
    checkNum = 1
    for range in currRanges:
        checkNum *= 1 + range[1] - range[0]
    if gt:
        oldLow = currRanges[val][0]
        oldHigh = currRanges[val][1]
        if oldLow <= newVal:
            currRanges[val] = [oldLow, newVal]
            returnTotal += decisionTree(key, step + 1, currRanges)
        if oldHigh > newVal:
            currRanges[val] = [newVal + 1, oldHigh]
            returnTotal += decisionTree(insuction[insuction.index(':') + 1:], 0, currRanges)
        currRanges[val] = [oldLow, oldHigh]
        return returnTotal
    else:
        oldLow = currRanges[val][0]
        oldHigh = currRanges[val][1]
        if oldLow < newVal:
            currRanges[val] = [oldLow, newVal - 1]
            returnTotal += decisionTree(insuction[insuction.index(':') + 1:], 0, currRanges)
        if oldHigh >= newVal:
            currRanges[val] = [newVal, oldHigh]
            returnTotal += decisionTree(key, step + 1, currRanges)
        currRanges[val] = [oldLow, oldHigh]
        return returnTotal

startRanges = [[1, 4000] for _ in range(4)]
print(decisionTree('in', 0, startRanges))
       