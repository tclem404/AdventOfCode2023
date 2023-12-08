import fileinput
import copy
import numpy

sum = 0
graph = list(fileinput.input(files=['Day8/val.txt']))
instructions = [int(x) for x in graph[0].replace('L', '0').replace('R','1').replace('\n','')]
graph = graph[2:]

currPos = []
for x in graph:
    if x[2] == 'A':
        currPos.append(x[0:3])

dictionary = dict([(x[0:3], [x[7:10], x[12:15]]) for x in graph])

cycleLen = []
for i in range(len(currPos)):
    step = 0
    possible = 0
    while currPos[i][2] != 'Z':
        currPos[i] = dictionary[currPos[i]][instructions[(step) % len(instructions)]]
        step += 1
    cycleLen.append(step)
    print(numpy.lcm(step, len(instructions)) == step)

# note, this solution only works as all the paths are cyclic in line with the path
# this is because they take a certain number of instruction cycles to cycle, hence all the
# true prints

# this is not a solution for a general application, but that is not what this
# advent calendar is really about
currLcm = 1
for x in cycleLen:
    currLcm = numpy.lcm(x, currLcm, dtype=object)

print(currLcm)

    