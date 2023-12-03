import fileinput

sum = 0
textArr = []
for line in fileinput.input(files=['Day3/val.txt']):
    line = line.lower()
    line = line.replace('\n', '')
    textArr.append(line)
    
i = 0
while i < (len(textArr)): 
    j = 0
    while j < (len(textArr[i])):
        currNum = 0
        if(textArr[i][j] == '*'):
            y = max(0, i-1)
            ratio1 = -1
            while y < min(i+2, len(textArr)):
                x = max(0, j - 1)
                while x < min(j+2, len(textArr[y])):
                    if(textArr[y][x].isdigit()):
                        while (x <  len(textArr[y]) and textArr[y][x].isdigit()):
                            x += 1
                        pos = x - 1
                        power = 0
                        currNum = 0
                        while pos >= 0 and textArr[y][pos].isdigit():
                            currNum += int(textArr[y][pos])*(10**power)
                            power+= 1
                            pos -= 1

                        if ratio1 == -1:
                            ratio1 = currNum
                        else:
                            sum += ratio1*currNum
                            ratio1 = 0

                    x += 1

                y += 1
            
        j += 1
    i += 1
            

print(sum)