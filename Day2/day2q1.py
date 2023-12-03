import fileinput

sum = 0
for line in fileinput.input(files=['Day2/val.txt']):
    line = line.lower()
    line = line.replace("game", '')
    line = line.replace(" ", '')
    line = line.replace('red', " - 12")
    line = line.replace('green', " - 13")
    line = line.replace('blue', " - 14")
    line = line.split(":")
    line[1] = line[1].split(";")
    flag = 0
    for situation in line[1]:
        for showing in situation.split(","):
            if(eval(showing) > 0):
                flag = 1
                break

    if flag == 0:
        sum += int(line[0])

print(sum)