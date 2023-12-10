import fileinput

pipeMap = [x.replace('\n','') for x in list(fileinput.input(files=['Day10/val.txt']))]

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

maxRows = [max(x) for x in distances]
print(max(maxRows))
