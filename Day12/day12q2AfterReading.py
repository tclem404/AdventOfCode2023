import fileinput
from functools import cache

springLists = [x.replace('\n','').split(' ') for x in list(fileinput.input(files=['Day12/val.txt']))]
springLists = [[list(x[0]), [int(y) for y in x[1].split(',')]] for x in springLists]

# from https://www.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/
# spent nearly 2 hours on my try, but its finals week so I had to give up
# still spent time understanding this solution
@cache
def recusrionFunc(springMapping, springIndividuals, result = 0):
    if not springIndividuals:
        if '#' in springMapping:
            return 0
        return 1
    
    currSpring = springIndividuals[0]
    newSprings = springIndividuals[1:]
    for i in range(len(springMapping) - sum(newSprings) - len(newSprings) - currSpring + 1):
        if '#' in springMapping[:i]: break

        nextVal = i + currSpring
        if nextVal <= len(springMapping) and '.' not in springMapping[i : nextVal] and springMapping[nextVal:nextVal+1] != '#':
            result += recusrionFunc(springMapping[nextVal + 1:], newSprings)
    
    return result

total = 0
for x in springLists: 
    x[0].append('?')
    largeLine = []
    largeSet = []
    for i in range(5):
        for y in x[0]: largeLine.append(y)
        for y in x[1]: largeSet.append(y)
        
    largeLine.pop()

    largeLine = ''.join(largeLine)
    largeSet = tuple(largeSet)

    total += recusrionFunc(largeLine, largeSet)

print(total)