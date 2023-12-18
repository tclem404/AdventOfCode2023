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
        if j + 3 < len(mapping[i]): 
            miniSum = sum(mapping[i][j+1:j+4])
            for dist in range(4, 11, 1):
                if j + dist >= len(mapping[i]): break
                miniSum += mapping[i][j+dist]
                heapIns(minHeap, [currCost + miniSum + distanceToEnd - dist, i, j+dist, 1])
        
        if j - 3 >= 0: 
            miniSum = sum(mapping[i][j-3:j])
            for dist in range(4, 11, 1):
                if j - dist < 0: break
                miniSum += mapping[i][j-dist]
                heapIns(minHeap, [currCost + miniSum + distanceToEnd + dist, i, j-dist, 3])

    if dir != 2 and dir != 4:
        if i + 3 < len(mapping): 
            miniSum = 0
            for dist in range(1, 4, 1):
                miniSum += mapping[i + dist][j]
            
            for dist in range(4, 11, 1):
                if i + dist >= len(mapping): break
                miniSum += mapping[i+dist][j]
                heapIns(minHeap, [currCost + miniSum + distanceToEnd - dist, i + dist, j, 2])
        
        if i - 3 >= 0: 
            miniSum = 0
            for dist in range(1, 4, 1):
                miniSum += mapping[i - dist][j]
            
            for dist in range(4, 11, 1):
                if i - dist < 0: break
                miniSum += mapping[i-dist][j]
                heapIns(minHeap, [currCost + miniSum + distanceToEnd + dist, i - dist, j, 4])