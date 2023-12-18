import fileinput

mapping = [[int(y) for y in list(x.replace('\n',''))] for x in list(fileinput.input(files=['Day17/val.txt']))]

def heapIns(heapArr, elemArr):
    currInd = len(heapArr)
    heapArr.append(elemArr)
    while (currInd - 1) // 2 >= 0 and heapArr[(currInd - 1) // 2][0] > heapArr[currInd][0]:
        temp = heapArr[currInd]
        heapArr[currInd] = heapArr[(currInd - 1) // 2]
        heapArr[(currInd - 1) // 2] = temp
        currInd = (currInd - 1) // 2

def heapPop(heapArr):
    if len(heapArr) == 1: return heapArr.pop()
    head = heapArr.pop(0)
    heapArr.insert(0, heapArr.pop())
    currInd = 0
    while ((2 * currInd + 1 < len(heapArr) and heapArr[currInd][0] > heapArr[2 * currInd + 1][0]) or
          (2 * currInd + 2 < len(heapArr) and heapArr[currInd][0] > heapArr[2* currInd + 2][0])):
        minInd = 2 * currInd + 1
        if 2 * currInd + 2 < len(heapArr) and heapArr[2 * currInd + 2][0] < heapArr[2 * currInd + 1][0]: minInd += 1
        temp = heapArr[currInd]
        heapArr[currInd] = heapArr[minInd]
        heapArr[minInd] = temp
        currInd = minInd
    
    return head

minHeap = [[len(mapping) - 1 + len(mapping[-1]) - 1, 0, 0, 0]]
cost = [[[-1, -1] for _ in x] for x in mapping]
cost[0][0][1] = 0

while len(minHeap) > 0:
    currCost, i, j, dir = heapPop(minHeap)
    if cost[i][j][dir % 2] != -1 and cost[i][j][dir % 2] < currCost: continue 
    distanceToEnd = len(mapping) - 1 - i + len(mapping[-1]) - 1 - j
    currCost -= distanceToEnd
    cost[i][j][dir % 2] = currCost
    if min(cost[-1][-1]) != -1:
        print(cost[-1][-1])
        break
    if dir != 1 and dir != 3:
        if j + 1 < len(mapping[i]): heapIns(minHeap, [currCost + mapping[i][j + 1] + distanceToEnd - 1, i, j + 1, 1])
        if j + 2 < len(mapping[i]): heapIns(minHeap, [currCost + mapping[i][j + 1] + mapping[i][j + 2] + distanceToEnd - 2, i, j + 2, 1])
        if j + 3 < len(mapping[i]): heapIns(minHeap, [currCost + mapping[i][j + 1] + mapping[i][j + 2] + mapping[i][j + 3] + distanceToEnd - 3, i, j + 3, 1])
        if j - 1 >= 0: heapIns(minHeap, [currCost + mapping[i][j - 1] + distanceToEnd + 1, i, j - 1, 3])
        if j - 2 >= 0: heapIns(minHeap, [currCost + mapping[i][j - 1] + mapping[i][j - 2] + distanceToEnd + 2, i, j - 2, 3])
        if j - 3 >= 0: heapIns(minHeap, [currCost + mapping[i][j - 1] + mapping[i][j - 2] + mapping[i][j - 3] + distanceToEnd + 3, i, j - 3, 3])
    if dir != 2 and dir != 4:
        if i + 1 < len(mapping): heapIns(minHeap, [currCost + mapping[i+1][j] + distanceToEnd - 1, i+1, j, 2])
        if i + 2 < len(mapping): heapIns(minHeap, [currCost + mapping[i+1][j] + mapping[i+2][j] + distanceToEnd - 2, i+2, j, 2])
        if i + 3 < len(mapping): heapIns(minHeap, [currCost + mapping[i+1][j] + mapping[i+2][j] + mapping[i+3][j] + distanceToEnd - 3, i+3, j, 2])
        if i - 1 >= 0: heapIns(minHeap, [currCost + mapping[i-1][j] + distanceToEnd + 1, i-1, j, 4])
        if i - 2 >= 0: heapIns(minHeap, [currCost + mapping[i-1][j] + mapping[i-2][j] + distanceToEnd + 2, i-2, j, 4])
        if i - 3 >= 0: heapIns(minHeap, [currCost + mapping[i-1][j] + mapping[i-2][j] + mapping[i-3][j] + distanceToEnd + 3, i-3, j, 4])
