import fileinput

def reflectionChecker(arr, old):
    for i in range(1, len(arr)):
        if arr[max(0, 2*i - len(arr)):i] == arr[min(2 * i - 1, len(arr) - 1):i - 1:-1] and [i, i - max(0, 2*i - len(arr))] != old: return [i, i - max(0, 2*i - len(arr))]
    return [0,0]

images = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day13/val.txt']))]
dividedImages = [[]]
for x in images:
    if x == []:
        dividedImages.append([])
        continue

    dividedImages[-1].append(x)

total = 0
for image in dividedImages:
    curRows = list(range(len(image)))
    for i in range(len(image) - 1):
        if curRows[i] != i: continue

        for j in range(i + 1, len(image)):
            if image[i] == image[j]: curRows[j] = i

    foundRow = reflectionChecker(curRows, [0,0])
    new = 0

    similarRows = []
    for i in range(len(image) - 1):
        for j in range(i + 1, len(image)):
            check = 0
            for k in range(len(image[i])): 
                if image[i][k] == image[j][k]: check += 1
            
            if check == len(image[i]) - 1: similarRows.append([i,j])
    
    for swap in similarRows:
        temp = curRows[swap[0]]
        curRows[swap[0]] = curRows[swap[1]]
        newRef = reflectionChecker(curRows, foundRow)
        if newRef != foundRow and newRef[0] != 0: 
            total += 100 * newRef[0]
            foundRow = newRef
            new = 1
            break
        curRows[swap[0]] = temp
        temp = curRows[swap[1]]
        curRows[swap[1]] = curRows[swap[0]]
        newRef = reflectionChecker(curRows, foundRow)
        if newRef != foundRow and newRef[0] != 0: 
            total += 100 * newRef[0]
            foundRow = newRef
            new = 1
            break
        curRows[swap[1]] = temp


    if new == 0:
        transPose = [[] for _ in range(len(image[0]))]
        for row in image:
            for i in range(len(row)):
                transPose[i].append(row[i])
        
        curCols = list(range(len(transPose)))
        for i in range(len(transPose) - 1):
            if curCols[i] != i: continue

            for j in range(i + 1, len(transPose)):
                if transPose[i] == transPose[j]: curCols[j] = i

        foundCol = reflectionChecker(curCols, [0,0])

        similarCols = []
        for i in range(len(transPose) - 1):
            for j in range(i + 1, len(transPose)):
                check = 0
                for k in range(len(transPose[i])): 
                    if transPose[i][k] == transPose[j][k]: check += 1
                
                if check == len(transPose[i]) - 1: similarCols.append([i,j])
        
        for swap in similarCols:
            temp = curCols[swap[0]]
            curCols[swap[0]] = curCols[swap[1]]
            newRef = reflectionChecker(curCols, foundCol)
            if newRef != foundCol and newRef[0] != 0: 
                total += newRef[0]
                new = 1
                break
            curCols[swap[0]] = temp
            temp = curCols[swap[1]]
            curCols[swap[1]] = curCols[swap[0]]
            newRef = reflectionChecker(curCols, foundCol)
            if newRef != foundCol and newRef[0] != 0: 
                total += newRef[0]
                new = 1
                break
            curCols[swap[1]] = temp

print(total)