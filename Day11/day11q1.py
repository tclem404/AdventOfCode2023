import fileinput

galaxyMap = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day11/val.txt']))]

i = 0
while i < len(galaxyMap):
    if '#' not in galaxyMap[i]:
        galaxyMap.insert(i,['.']*len(galaxyMap[i]))
        i += 1
    i += 1


j = 0
while j < len(galaxyMap[0]):
    if '#' not in [x[j] for x in galaxyMap]:
        for i in range(len(galaxyMap)):
            galaxyMap[i].insert(j,'.')
        j += 1
    j += 1

galaxies = []
for i in range(len(galaxyMap)):
    for j in range(len(galaxyMap[0])):
        if galaxyMap[i][j] == '#':
            galaxies.append([i,j])

totalDist = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        totalDist += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(totalDist)