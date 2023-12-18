import fileinput

instructions = [list(x.split(' ')[2])[2:8] for x in list(fileinput.input(files=['Day18/val.txt']))]

for i in range(len(instructions)):
    oldLine = instructions[i]
    instructions[i] = []
    newDir = oldLine.pop()
    match newDir:
        case '0': instructions[i].append('R')
        case '1': instructions[i].append('D')
        case '2': instructions[i].append('L')
        case '3': instructions[i].append('U')

    instructions[i].append(int(''.join(oldLine),16))

endPoints = [[0,0]]
x = 0
y = 0
horizSide = 'L' # get from input, depends on what is considered inside
vertSide = 'D'
for i in range(len(instructions)):
    numMoves = int(instructions[i][1])
    match instructions[i][0]:
        case 'U':
            y += numMoves
            if i + 1 == len(instructions) or instructions[i+1][0] != horizSide: 
                if vertSide != 'U':
                    vertSide = 'U'
                    y += 1
            elif vertSide != 'D':
                vertSide = 'D'
                y -= 1
        case 'D':
            y -= numMoves
            if i + 1 == len(instructions) or instructions[i+1][0] != horizSide: 
                if vertSide != 'D':
                    vertSide = 'D'
                    y -= 1
            elif vertSide != 'U':
                vertSide = 'U'
                y += 1
        case 'L':
            x -= numMoves
            if i + 1 == len(instructions) or instructions[i+1][0] != vertSide: 
                if horizSide != 'L':
                    x -= 1
                    horizSide = 'L'
            elif horizSide != 'R':
                horizSide = 'R'
                x += 1
        case 'R':
            x += numMoves
            if i + 1 == len(instructions) or instructions[i+1][0] != vertSide: 
                if horizSide != 'R':
                    x += 1
                    horizSide = 'R'
            elif horizSide != 'L':
                horizSide = 'L'
                x -= 1
    endPoints.append([x,y])


polyArea = 0
for i in range(len(endPoints) - 1):
    polyArea += endPoints[i][0] * endPoints[(i+1)][1] - endPoints[i][1] * endPoints[(i+1)][0]
polyArea = polyArea // 2
print(abs(polyArea)) # always take the largest area I think, dunno