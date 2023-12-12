import fileinput
import copy

springLists = [x.replace('\n','').split(' ') for x in list(fileinput.input(files=['Day12/val.txt']))]
springLists = [[list(x[0]), [int(y) for y in x[1].split(',')]] for x in springLists]

def possible(springArr):
    if '?' in springArr[0] and '.' in springArr[0]:
        indexOfQ = 0
        result = 0
        if springArr[0].index('?') < springArr[0].index('.'):
            indexOfQ = springArr[0].index('?')
            springArr[0][indexOfQ] = '.'
            result = countPatterns([springArr[0][indexOfQ:], springArr[1]])
            springArr[0][indexOfQ] = '?'
        else:
            indexOfQ = springArr[0].index('.')
            result = countPatterns(springArr[0][indexOfQ:])
        if result != 0:
            return indexOfQ + possible([springArr[0][indexOfQ + 1:], springArr[1]])
        return 0
    elif '?' in springArr[0]:
        indexOfQ = springArr[0].index('?')
        springArr[0][indexOfQ] = '.'
        result = countPatterns([springArr[0][indexOfQ:], springArr[1]])
        springArr[0][indexOfQ] = '?'
        if result != 0:
            return indexOfQ + possible([springArr[0][indexOfQ + 1:], springArr[1]])
        return 0
    elif '.' in springArr[0]:
        indexOfQ = springArr[0].index('?')
        result = countPatterns([springArr[0][indexOfQ:], springArr[1]])
        if result != 0:
            return indexOfQ + possible([springArr[0][indexOfQ + 1:], springArr[1]])
        return 0
    return 0


def countPatterns(springArr):

    quickCheck = (''.join(copy.deepcopy(springArr[0]))).replace('?', '.')
    quickCheckLens = [len(x) for x in quickCheck.split('.') if x != '']
    if max(quickCheckLens) > max(springArr[1]):
            return 0
    if min(quickCheckLens) < min(springArr[1]):
            return 0
    
    if '?' in springArr[0]:
        indexOfQ = springArr[0].index('?')
        springArr[0][indexOfQ] = '.'
        partial = countPatterns(springArr)
        springArr[0][indexOfQ] = '#'
        partial += countPatterns(springArr)
        springArr[0][indexOfQ] = '?'
        return partial
    else:
        if [len(x) for x in ''.join(springArr[0]).split('.') if x != ''] == springArr[1]:
            return 1
        return 0

total = 0
for x in springLists:
    if x[0][-1] == '.':
        totalAddition = countPatterns(x)
        x[0].insert(0,'?')
        totalAddition = totalAddition * (countPatterns(x) ** 4)
        total += totalAddition
        # print(totalAddition)
    elif x[0][0] == '.':
        totalAddition = countPatterns(x)
        x[0].append('?')
        totalAddition = totalAddition * (countPatterns(x) ** 4)
        total += totalAddition
        # print(totalAddition)
    elif x[0][-1] == '#' and x[0][0] == '#':
        x[0].append('?')
        largeLine = []
        largeSet = []
        for i in range(5):
            for y in x[0]: largeLine.append(y)
            for y in x[1]: largeSet.append(y)
        
        largeLine.pop()
        totalAddition = countPatterns([largeLine, largeSet])
        total += totalAddition
        print(totalAddition)
    elif x[0][0] == '?':
        if x[0][-1] == '#':
            x[0][0] = '.'
            totalAddition = countPatterns(x)
            x[0].append('?')
            totalAddition += totalAddition * (countPatterns(x) ** 4)
            x[0].pop()
            x[0][0] = '#'
            totalAddition += countPatterns(x) ** 5
            # print(totalAddition)
            total += totalAddition
        else: # must be '?' as well
            # print('here')
            # print(x[0])
            x[0][0] = '.'
            totalAddition = countPatterns(x)
            x[0].append('?')
            # print(x[0])
            totalAddition = totalAddition * (countPatterns(x) ** 4)
            total += totalAddition
            x[0].pop()
            x[0][0] = '?'
            # print(x[0])
            x[0][-1] = '.'
            totalAddition2 = countPatterns(x)
            x[0].insert(0,'?')
            # print(x[0])
            totalAddition2 = totalAddition2 * (countPatterns(x) ** 4)
            total += totalAddition2
            x[0][1] = '.'
            overlap = countPatterns(x) ** 4
            x[0].pop(0)
            overlap = overlap * countPatterns(x)
            total -= overlap
            x[0][0] = '#'
            x[0][-1] = '#'
            # print(x[0])
            totalAddition3 = countPatterns(x) ** 5
            total += totalAddition3
            # print(totalAddition)
            # print(totalAddition2)
            # print(totalAddition3)
            # print('out')
    else: # x[0][-1] == '?' and x[0][0] == '#'
        x[0][-1] = '.' # case of # and .
        totalAddition = countPatterns(x)
        x[0].insert(0,'?')
        totalAddition = totalAddition * (countPatterns(x) ** 4)
        total += totalAddition
        x[0].pop(0)
        x[0][-1] = '#' # case of # and #
        totalAddition2 = countPatterns(x) ** 5
        total += totalAddition2
        # print(totalAddition2)  

print(total)
