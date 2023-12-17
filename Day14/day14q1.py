import fileinput

rocks = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day14/val.txt']))]

total = 0
for j in range(len(rocks[0])):
    rockPosList = []
    currPos = 0
    for i in range(len(rocks)):
        if rocks[i][j] == 'O':
            rockPosList.append(len(rocks) - currPos)
            currPos += 1
        elif rocks[i][j] == '#':
            currPos = i + 1
    
    total += sum(rockPosList)

print(total)