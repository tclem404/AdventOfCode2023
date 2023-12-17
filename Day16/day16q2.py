import fileinput

mirrorMap = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day16/val.txt']))]

def findVal(init):
    visitedSplitters = []

    energized = [[] for _ in range(len(mirrorMap))]

    posQueue = [init]
    while len(posQueue) > 0:
        i,j,dir = posQueue.pop(0)
        if [i,j,dir] in visitedSplitters: continue
        if j not in energized[i]: energized[i].append(j)
        match dir:
            case 1: # left
                match mirrorMap[i][j]:
                    case '.':
                        if j + 1 < len(mirrorMap[i]): posQueue.append([i, j + 1, 1])
                    case '-':
                        if j + 1 < len(mirrorMap[i]): posQueue.append([i, j + 1, 1])
                    case '\\':
                        if i + 1 < len(mirrorMap): posQueue.append([i + 1, j, 2])
                    case '/':
                        if i - 1 >= 0: posQueue.append([i - 1, j, 4])
                    case '|':
                        visitedSplitters.append([i,j,1])
                        visitedSplitters.append([i,j,3])
                        if i + 1 < len(mirrorMap): posQueue.append([i + 1, j, 2])
                        if i - 1 >= 0: posQueue.append([i - 1, j, 4])
            case 2:
                match mirrorMap[i][j]:
                    case '.':
                        if i + 1 < len(mirrorMap): posQueue.append([i + 1, j, 2])
                    case '|':
                        if i + 1 < len(mirrorMap): posQueue.append([i + 1, j, 2])
                    case '\\':
                        if j + 1 < len(mirrorMap[i]): posQueue.append([i, j + 1, 1])
                    case '/':
                        if j - 1 >= 0: posQueue.append([i, j - 1, 3])
                    case '-':
                        visitedSplitters.append([i,j,2])
                        visitedSplitters.append([i,j,4])
                        if j - 1 >= 0: posQueue.append([i, j - 1, 3])
                        if j + 1 < len(mirrorMap[i]): posQueue.append([i, j + 1, 1])
            case 3:
                match mirrorMap[i][j]:
                    case '.':
                        if j - 1 >= 0: posQueue.append([i, j - 1, 3])
                    case '-':
                        if j - 1 >= 0: posQueue.append([i, j - 1, 3])
                    case '\\':
                        if i - 1 >= 0: posQueue.append([i - 1, j, 4])
                    case '/':
                        if i + 1 < len(mirrorMap): posQueue.append([i + 1, j, 2])
                    case '|':
                        visitedSplitters.append([i,j,1])
                        visitedSplitters.append([i,j,3])
                        if i + 1 < len(mirrorMap): posQueue.append([i + 1, j, 2])
                        if i - 1 >= 0: posQueue.append([i - 1, j, 4])
            case 4:
                match mirrorMap[i][j]:
                    case '.':
                        if i - 1 >= 0: posQueue.append([i - 1, j, 4])
                    case '|':
                        if i - 1 >= 0: posQueue.append([i - 1, j, 4])
                    case '\\':
                        if j - 1 >= 0: posQueue.append([i, j - 1, 3])
                    case '/':
                        if j + 1 < len(mirrorMap[i]): posQueue.append([i, j + 1, 1])
                    case '-':
                        visitedSplitters.append([i,j,2])
                        visitedSplitters.append([i,j,4])
                        if j + 1 < len(mirrorMap[i]): posQueue.append([i, j + 1, 1])
                        if j - 1 >= 0: posQueue.append([i, j - 1, 3])

    return (sum([len(x) for x in energized]))

maxVal = -1
for i in range(len(mirrorMap)):
    leftVal = findVal([i,0,1])
    rightVal = findVal([i,len(mirrorMap[i]) - 1,3])
    maxVal = max([leftVal, rightVal, maxVal])
for j in range(len(mirrorMap[0])):
    leftVal = findVal([0,j,2])
    rightVal = findVal([len(mirrorMap) - 1,j,4])
    maxVal = max([leftVal, rightVal, maxVal])

print(maxVal)