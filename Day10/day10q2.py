import fileinput
import copy

pipeMap = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day10/val.txt']))]

queue = []

distances = [[0] * len(pipeMap[i]) for i in range(len(pipeMap))]

sPos = []
for i in range(len(pipeMap)):
    if 'S' in pipeMap[i]:
        sPos = [i, pipeMap[i].index('S')]
        break

distances[sPos[0]][sPos[1]] = -1

if sPos[0] + 1 != len(pipeMap) and pipeMap[sPos[0] + 1][sPos[1]] in '|7F':
    queue.append([sPos[0] + 1, sPos[1],1])
if sPos[0] - 1 != -1 and pipeMap[sPos[0] - 1][sPos[1]] in '|LJ':
    queue.append([sPos[0] - 1, sPos[1],1])
if sPos[1] + 1 != len(pipeMap[sPos[0]]) and pipeMap[sPos[0]][sPos[1] + 1] in '-J7':
    queue.append([sPos[0], sPos[1] + 1,1])
if sPos[1] - 1 != -1 and pipeMap[sPos[0]][sPos[1] - 1] in '-J7':
    queue.append([sPos[0], sPos[1] - 1,1])

while len(queue) > 0:
    currPos = queue.pop(0)
    if distances[currPos[0]][currPos[1]] != 0: continue
    distances[currPos[0]][currPos[1]] = currPos[2]
    currChar = pipeMap[currPos[0]][currPos[1]]
    if currChar == '|':
        if currPos[0] + 1 != len(pipeMap): queue.append([currPos[0] + 1, currPos[1], currPos[2] + 1])
        if currPos[0] - 1 != -1: queue.append([currPos[0] - 1, currPos[1], currPos[2] + 1])
    elif currChar == '-':
        if currPos[1] + 1 != len(pipeMap[currPos[0]]): queue.append([currPos[0], currPos[1] + 1, currPos[2] + 1])
        if currPos[1] - 1 != -1: queue.append([currPos[0], currPos[1] - 1, currPos[2] + 1])
    elif currChar == 'L':
        if currPos[0] - 1 != -1: queue.append([currPos[0] - 1, currPos[1], currPos[2] + 1])
        if currPos[1] + 1 != len(pipeMap[currPos[0]]): queue.append([currPos[0], currPos[1] + 1, currPos[2] + 1])
    elif currChar == 'J':
        if currPos[0] - 1 != -1: queue.append([currPos[0] - 1, currPos[1], currPos[2] + 1])
        if currPos[1] - 1 != -1: queue.append([currPos[0], currPos[1] - 1, currPos[2] + 1])
    elif currChar == '7':
        if currPos[0] + 1 != len(pipeMap): queue.append([currPos[0] + 1, currPos[1], currPos[2] + 1])
        if currPos[1] - 1 != -1: queue.append([currPos[0], currPos[1] - 1, currPos[2] + 1])
    elif currChar == 'F':
        if currPos[0] + 1 != len(pipeMap): queue.append([currPos[0] + 1, currPos[1], currPos[2] + 1])
        if currPos[1] + 1 != len(pipeMap[currPos[0]]): queue.append([currPos[0], currPos[1] + 1, currPos[2] + 1])

for i in range(len(pipeMap)):
    for j in range(len(pipeMap[i])):
        if distances[i][j] == 0: pipeMap[i][j] = '.'

extendedMap = []

for x in pipeMap:
    extendedMap.append(['.'] * (2*len(x) - 1))
    extendedMap.append(['.'] * (2*len(x) - 1))
extendedMap.pop()

for i in list(range(len(pipeMap))):
    for j in list(range(len(pipeMap[i]))):
        extendedMap[2*i][2*j] = pipeMap[i][j]
        if i + 1 < len(pipeMap) and pipeMap[i][j] in '|F7S' and pipeMap[i+1][j] in '|JLS':
            extendedMap[2*i + 1][2*j] = '|'
        if j + 1 < len(pipeMap[i]) and pipeMap[i][j] in '-FLS' and pipeMap[i][j + 1] in '-J7S':
            extendedMap[2*i][2*j + 1] = '-'

#strTest = ''.join([''.join(x) + '\n' for x in extendedMap])
#print(strTest)

queue = []

for i in range(len(extendedMap)):
    if extendedMap[i][0] == '.': queue.append([i, 0])
    if extendedMap[i][-1] == '.': queue.append([i, len(extendedMap[i]) - 1])

for i in range(len(extendedMap[0])):
    if extendedMap[0][i] == '.': queue.append([0, i])

for i in range(len(extendedMap[-1])):
    if extendedMap[-1][i] == '.': queue.append([len(extendedMap)-1, i])

while len(queue) > 0:
    currPos = queue.pop(0)
    if extendedMap[currPos[0]][currPos[1]] != '.': continue
    extendedMap[currPos[0]][currPos[1]] = '0'
    if currPos[0] - 1 >= 0: queue.append([currPos[0] - 1, currPos[1]])
    if currPos[0] + 1 < len(extendedMap): queue.append([currPos[0] + 1, currPos[1]])
    if currPos[1] - 1 > -1: queue.append([currPos[0], currPos[1] - 1])
    if currPos[1] + 1 < len(extendedMap[currPos[0]]): queue.append([currPos[0], currPos[1] + 1])

#strTest = ''.join([''.join(x) + '\n' for x in extendedMap])
#print(strTest)

finalMap = [[extendedMap[i][j] for j in range(0, len(extendedMap[i]), 2)] for i in range(0, len(extendedMap), 2)]

#strTest = ''.join([''.join(x) + '\n' for x in finalMap])
#print(strTest)

numZerosRow = [x.count('.') for x in finalMap]
print(sum(numZerosRow))