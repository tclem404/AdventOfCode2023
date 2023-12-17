import fileinput
import copy


rocks = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day14/val.txt']))]

endPositions = [copy.deepcopy(rocks)]
for cycle in range(1000000000):
    for j in range(len(rocks[0])):
        rockPosList = []
        currPos = 0
        for i in range(len(rocks)):
            if rocks[i][j] == 'O':
                rockPosList.append(len(rocks) - currPos)
                currPos += 1
                rocks[i][j] = '.'
            elif rocks[i][j] == '#':
                currPos = i + 1

        for i in rockPosList:
            rocks[len(rocks) - i][j] = 'O'
        
    for i in range(len(rocks)):
        rockPosList = []
        currPos = 0
        for j in range(len(rocks[i])):
            if rocks[i][j] == 'O':
                rockPosList.append(currPos)
                currPos += 1
                rocks[i][j] = '.'
            elif rocks[i][j] == '#':
                currPos = j + 1
        
        for j in rockPosList:
            rocks[i][j] = 'O'

    for j in range(len(rocks[0])):
        rockPosList = []
        currPos = len(rocks) - 1
        for i in range(len(rocks) - 1, -1, -1):
            if rocks[i][j] == 'O':
                rockPosList.append(currPos)
                currPos -= 1
                rocks[i][j] = '.'
            elif rocks[i][j] == '#':
                currPos = i - 1

        for i in rockPosList:
            rocks[i][j] = 'O'
        
    for i in range(len(rocks)):
        rockPosList = []
        currPos = len(rocks[i]) - 1
        for j in range(len(rocks[i]) - 1, -1, -1):
            if rocks[i][j] == 'O':
                rockPosList.append(currPos)
                currPos -= 1
                rocks[i][j] = '.'
            elif rocks[i][j] == '#':
                currPos = j - 1
        
        for j in rockPosList:
            rocks[i][j] = 'O'
        
    if rocks in endPositions:
        break
    else:
        endPositions.append(copy.deepcopy(rocks))

if cycle != 1000000000 - 1:
    endPositions = endPositions[endPositions.index(rocks):]
    rocks = endPositions[(1000000000 - 1 - cycle) % len(endPositions)]

total = 0
for i in range(len(rocks)):
    for j in range(len(rocks[i])):
        if rocks[i][j] == 'O': total += len(rocks) - i

print(total)