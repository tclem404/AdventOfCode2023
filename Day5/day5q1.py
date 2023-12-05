import fileinput

totalTxt = ''.join(list(fileinput.input(files=['Day5/val.txt'])))
totalTxt = totalTxt.split('\n\n')

for i in range(len(totalTxt)):
    totalTxt[i] = totalTxt[i].split(':')[1].split('\n')
    totalTxt[i] = [[int(y) for y in x.split(' ') if y.isnumeric()] for x in totalTxt[i]]

currMapping = totalTxt[0][0]

for mapping in totalTxt[1:]:
    for shift in mapping:
        if shift != []:
            startDestination = shift[0]
            startFrom = shift[1]
            rangeOf = shift[2]
            for i in range(len(currMapping)):
                if currMapping[i] >= startFrom and currMapping[i] - startFrom < rangeOf:
                    currMapping[i] = -1* (startDestination + (currMapping[i] - startFrom))
    currMapping = [abs(x) for x in currMapping]

print(min(currMapping))
