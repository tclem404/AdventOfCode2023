import fileinput
from collections import Counter
import copy

sum = 0
hands = []
for line in fileinput.input(files=['Day7/val.txt']):
    hands.append(line.replace('\n','').split(' '))    
    hands[-1][1] = int(hands[-1][1])

handsTemp = copy.deepcopy(hands)
for i in range(len(handsTemp)):
    if 'J' in handsTemp[i][0] and handsTemp[i][0].replace('J','') != '':
        vals = list(Counter(handsTemp[i][0].replace('J','')).values())
        ind = 0
        for j in range(1, len(vals)): 
            if vals[ind] < vals[j]: ind = j
        handsTemp[i][0] = handsTemp[i][0].replace('J', list(Counter(handsTemp[i][0].replace('J','')).keys())[ind])

counts = [list(Counter(x[0]).values()) for x in handsTemp]
for i in range(len(counts)):
    if 5 == max(counts[i]): counts[i][0] = 7
    if 4 == max(counts[i]): counts[i][0] = 6
    if 3 in counts[i] and 2 in counts[i]: counts[i][0] = 5
    if 3 == max(counts[i]): counts[i][0] = 4
    if 2 == max(counts[i]) and len(counts[i]) == 3: counts[i][0] = 3

counts = [max(x) for x in counts]

rank = 1
for i in range(1,8):
    currConsideration = []
    for x in range(len(hands)):
        if counts[x] == i:
            currConsideration.append([hands[x][0].replace('K', 'B').replace('Q', 'C').replace('J', 'N').replace('T', 'E').replace('9', 'F').replace('8', 'G').replace('7', 'H').replace('6', 'I').replace('5', 'J').replace('4', 'K').replace('3', 'L').replace('2', 'M'), hands[x][1]])

    currConsideration.sort()

    for j in range(len(currConsideration) - 1, -1, -1):
        sum += currConsideration[j][1] * rank
        rank += 1

print(sum)