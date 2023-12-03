import fileinput

sum = 0
for line in fileinput.input(files=['Day2/val.txt']):
    line = line.lower()
    line = line.replace("game", '')
    line = line.replace(" ", '')
    line = line.split(":")
    line[1] = line[1].split(";")
    flag = 0
    maxes = [0,0,0]
    for situation in line[1]:
        for showing in situation.split(","):
            if('red' in showing):
                maxes[0] = max(maxes[0], int(showing.replace('red','')))
            elif('green' in showing):
                maxes[1] = max(maxes[1], int(showing.replace('green','')))
            else:
                maxes[2] = max(maxes[2], int(showing.replace('blue','')))

    sum += maxes[0]*maxes[1]*maxes[2]

print(sum)