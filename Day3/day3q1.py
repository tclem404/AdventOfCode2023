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
        if(textArr[i][j].isdigit()):
            rangeArr = [j-1,j+1]
            currNum = int(textArr[i][j])
            while rangeArr[1] < len(textArr[i]) and textArr[i][rangeArr[1]].isdigit():
                currNum = 10 * currNum + int(textArr[i][rangeArr[1]])
                rangeArr[1] += 1
            j = rangeArr[1]
            
            checkArr = textArr[max(i-1, 0) : min(i+1, len(textArr)-1) + 1]
            for line in checkArr:
                line = line[max(rangeArr[0], 0) : min(rangeArr[1], len(textArr[i])- 1) + 1]
                for char in line:
                    if(char != '.' and not char.isdigit()):
                        sum += currNum
                        currNum = 0
                        break
        j += 1
    i += 1
            


print(sum)