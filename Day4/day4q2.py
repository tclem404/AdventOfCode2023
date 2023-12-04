import fileinput

def calcCard(index):
    if cardVals[index] == -1:
        line = cards[index]
        line = line.split("|")
        winningNums = [int(x) for x in line[0].split(' ') if x.isnumeric()]
        numsHave = [int(x) for x in line[1].split(' ') if x.isnumeric()]
        count = len([x for x in numsHave if x in winningNums])

        sum = 1
        if count > 0:
            for i in range(count):
                sum = sum + calcCard(index + i + 1)
        cardVals[index] = sum
        return sum
    else:
        return cardVals[index]

cards = list(fileinput.input(files=['Day4/val.txt']))
for i in range(len(cards)):
    cards[i] = cards[i].replace("\n","").split(":")[1]

cardVals = [-1] * len(cards)

total = 0
for i in range(len(cards)):
    total += calcCard(i)

print(total)