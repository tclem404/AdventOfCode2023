import fileinput

galaxyMap = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day11/val.txt']))]

rowsExpand = []
colsExpand = []

i = 0
while i < len(galaxyMap):
    if '#' not in galaxyMap[i]:
        rowsExpand.append(i)
    i += 1


j = 0
while j < len(galaxyMap[0]):
    if '#' not in [x[j] for x in galaxyMap]:
        colsExpand.append(j)
    j += 1

galaxies = []
for i in range(len(galaxyMap)):
    for j in range(len(galaxyMap[0])):
        if galaxyMap[i][j] == '#':
            galaxies.append([i,j])

totalDist = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        for x in rowsExpand:
            if x in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0]) + 1): totalDist += 999999
        for x in colsExpand:
            if x in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1]) + 1): totalDist += 999999
        totalDist += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(totalDist)