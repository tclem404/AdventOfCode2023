import fileinput

springLists = [x.replace('\n','').split(' ') for x in list(fileinput.input(files=['Day12/val.txt']))]
springLists = [[list(x[0]), [int(y) for y in x[1].split(',')]] for x in springLists]

def countPatterns(springArr):
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
    addToTotal = countPatterns(x)
    total += addToTotal

print(total)