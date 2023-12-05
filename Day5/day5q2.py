import fileinput

totalTxt = ''.join(list(fileinput.input(files=['Day5/val.txt'])))
totalTxt = totalTxt.split('\n\n')

for i in range(len(totalTxt)):
    totalTxt[i] = totalTxt[i].split(':')[1].split('\n')
    totalTxt[i] = [[int(y) for y in x.split(' ') if y.isnumeric()] for x in totalTxt[i]]

seedRanges = totalTxt[0][0]
currMapping = []
for i in range(0,len(seedRanges),2):
    currMapping.append([seedRanges[i], seedRanges[i+1]])

for mapping in totalTxt[1:]:
    #print(currMapping)
    for shift in mapping:
        if shift != []:
            startDestination = shift[0]
            startFrom = shift[1]
            rangeOf = shift[2]
            for i in range(len(currMapping)):
                #print(currMapping[i][0] - startFrom, startFrom - sum(currMapping[i]))
                if currMapping[i][0] <= startFrom and startFrom < sum(currMapping[i]):
                    if sum(currMapping[i]) <= startFrom + rangeOf:
                        currMapping.append([-1 * startDestination, -1 * (sum(currMapping[i]) - startFrom)])
                        currMapping[i][1] -= sum(currMapping[i]) - startFrom
                    else:
                        currMapping.append([-1*startDestination, -1*rangeOf])
                        currMapping.append([(startFrom + rangeOf), (sum(currMapping[i]) - startFrom - rangeOf)])
                        currMapping[i][1] -= sum(currMapping[i]) - startFrom
                if startFrom < currMapping[i][0] and startFrom + rangeOf >= sum(currMapping[i]):
                    currMapping[i][0] = -1*(startDestination + (currMapping[i][0] - startFrom))
                    currMapping[i][1] *= -1
                elif startFrom < currMapping[i][0] and startFrom + rangeOf > currMapping[i][0]:
                    currMapping.append([-1*(startDestination + currMapping[i][0] - startFrom), -1*(startFrom + rangeOf - currMapping[i][0])])
                    currMapping[i] = [startFrom + rangeOf, sum(currMapping[i]) - (startFrom + rangeOf)]


    currMapping = [[abs(y) for y in x] for x in currMapping if x[1] != 0]

# meta solving, want 0 to not be answer, check next one
# not good solution, but it works
print(min(currMapping))