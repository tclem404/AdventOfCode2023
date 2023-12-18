import fileinput

instructions = [x.split(' ')[0:2] for x in list(fileinput.input(files=['Day18/val.txt']))]

lines = {0:[0]}

x = 0
y = 0
for line in instructions:
    numMoves = int(line[1])
    match line[0]:
        case 'U':
            for i in range(1, numMoves + 1):
                if y + i in lines:
                    if x not in lines[y + i]: lines[y + i].append(x)
                else:
                    lines[y + i] = [x]
            y += numMoves
        case 'D':
            for i in range(1, numMoves + 1):
                if y - i in lines:
                    if x not in lines[y - i]: lines[y - i].append(x)
                else:
                    lines[y - i] = [x]
            y -= numMoves
        case 'L':
            for i in range(1, numMoves + 1):
                if x - i not in lines[y]: lines[y].append(x - i)
            x -= numMoves
        case 'R':
            for i in range(1, numMoves + 1):
                if x + i not in lines[y]: lines[y].append(x + i)
            x += numMoves

for label in lines.keys():
    lines[label].sort()

queue = []
for label in lines.keys():
    if lines[label][1] - lines[label][0] > 1:
        queue.append([lines[label][0] + 1, label])
        break

while len(queue) > 0:
    x, y = queue.pop(0)
    if x in lines[y]: continue
    lines[y].append(x)
    queue.append([x+1,y])
    queue.append([x-1,y])
    queue.append([x,y+1])
    queue.append([x,y-1])

total = 0
for arr in lines.values():
    total += len(arr)

print(total)
        