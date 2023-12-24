import fileinput

instructions = [x.replace('\n', '') for x in list(fileinput.input(files=['Day19/val.txt']))]

partialDict = instructions[0:instructions.index('')]
objects = instructions[instructions.index('') + 1:]

for i, obj in enumerate(partialDict):
    partialDict[i] = '\"' + obj[0:obj.index('{')] + '\":' + str(obj[obj.index('{') + 1: -1].split(','))

dictionary = eval('{' + ','.join(partialDict) + '}')

total = 0
for obj in objects:
    vals = obj[1:-1].split(',')
    x = int(vals[0][2:]) ; m = int(vals[1][2:]); a = int(vals[2][2:]); s = int(vals[3][2:])
    currKey = 'in'
    while currKey != 'A' and currKey != 'R':
        rules = dictionary[currKey]
        for i, rule in enumerate(rules):
            if i == len(rules) - 1:
                currKey = rule
                break
            if eval(rule[0:rule.index(':')]):
                currKey = rule[rule.index(':') + 1:]
                break
    
    if currKey == 'A': total += x + m + a + s

print(total)
       