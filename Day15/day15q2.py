import fileinput

codes = list(fileinput.input(files=['Day15/val.txt']))[0].replace('\n','').split(',')

boxList = [[] for _ in range(256)]
total = 0
for currCode in codes:
    eql = False
    if '=' in currCode:
        currCode = currCode.split('=')
        currCode[1] = int(currCode[1])
        eql = True
    else:
        currCode = currCode.split('-')
    
    inputLens = list(currCode[0])
    hashVal = 0
    for character in inputLens:
        hashVal += ord(character)
        hashVal *= 17
        hashVal %= 256
    
    ind = -1
    for i in range(len(boxList[hashVal])):
        if boxList[hashVal][i][0] == currCode[0]:
            ind = i
            break
    
    if eql:
        if ind == -1:
            boxList[hashVal].append(currCode)
        else:
            boxList[hashVal][ind] = (currCode)
    elif ind != -1:
        boxList[hashVal].pop(ind)


for i in range(len(boxList)):
    if boxList[i] != []:
        for j in range(len(boxList[i])):
            total += (1 + i) * (1 + j) * boxList[i][j][1]
print(total)
