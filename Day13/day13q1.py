import fileinput

def reflectionChecker(arr):
    for i in range(1, len(arr)):
        if arr[max(0, 2*i - len(arr)):i] == arr[min(2 * i - 1, len(arr) - 1):i - 1:-1]: return i
    return 0

images = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day13/val.txt']))]
dividedImages = [[]]
for x in images:
    if x == []:
        dividedImages.append([])
        continue

    dividedImages[-1].append(x)

total = 0
foundRow = 0
for image in dividedImages:
    curRows = list(range(len(image)))
    for i in range(len(image) - 1):
        if curRows[i] != i: continue

        for j in range(i + 1, len(image)):
            if image[i] == image[j]: curRows[j] = i

    foundRow = reflectionChecker(curRows)
    total += 100 * foundRow

    if foundRow == 0:
        transPose = [[] for x in range(len(image[0]))]
        for row in image:
            for i in range(len(row)):
                transPose[i].append(row[i])
        
        curCols = list(range(len(transPose)))
        for i in range(len(transPose) - 1):
            if curCols[i] != i: continue

            for j in range(i + 1, len(transPose)):
                if transPose[i] == transPose[j]: curCols[j] = i

        total += reflectionChecker(curCols)

print(total)