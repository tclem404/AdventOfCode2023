import fileinput

sum = 0
graph = list(fileinput.input(files=['Day8/val.txt']))
instructions = [int(x) for x in graph[0].replace('L', '0').replace('R','1').replace('\n','')]
graph = graph[2:]

dictionary = dict([(x[0:3], [x[7:10], x[12:15]]) for x in graph])

step = 1
currPos = 'AAA'
while currPos != 'ZZZ':
    currPos = dictionary[currPos][instructions[(step - 1) % len(instructions)]]
    step += 1

print(step - 1)

    