import fileinput

mapping = [list(x.replace('\n','')) for x in list(fileinput.input(files=['Day21/val.txt']))]

queue = 0
for i, row in enumerate(mapping):
    if 'S' in row:
        queue = [[i, row.index('S'), 32]]
        break

totalPos = 0
while len(queue) > 0:
    x, y, steps = queue.pop(0)
    if steps < 0 or x < 0 or x >= len(mapping) or y < 0 or y >= len(mapping[x]) or mapping[x][y] in 'O#': continue

    mapping[x][y] = 'O'
    totalPos += 1
    if x + 1 < len(mapping) and mapping[x+1][y] == '.':
        queue.append([x+1, y+1, steps - 1])
        queue.append([x+1, y-1, steps - 1])
        queue.append([x+2, y, steps - 1])
    if x - 1 >= 0 and mapping[x-1][y] == '.':
        queue.append([x-1, y+1, steps - 1])
        queue.append([x-1, y-1, steps - 1])
        queue.append([x-2, y, steps - 1])
    if y + 1 < len(mapping[x]) and mapping[x][y+1] == '.':
        queue.append([x+1, y+1, steps - 1])
        queue.append([x-1, y+1, steps - 1])
        queue.append([x, y+2, steps - 1])
    if y - 1 >= 0 and mapping[x][y-1] == '.':
        queue.append([x+1, y-1, steps - 1])
        queue.append([x-1, y-1, steps - 1])
        queue.append([x, y-2, steps - 1])

print(totalPos)