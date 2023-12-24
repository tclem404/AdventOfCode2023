import fileinput
import copy

buttons = [x.replace('\n', '') for x in list(fileinput.input(files=['Day20/val.txt']))]

startIns = ''
buttonDict = {}
listOfKeys = []
ind = 0
for button in buttons:
    if button[0:button.index(' ')] == 'broadcaster':
        startIns = button[button.index(' ') + 4:].split(', ')
        continue
    
    buttonInfo = []
    if button[0] == '%': continue
    
    listOfKeys.append(button[1:button.index(' ')])

    buttonInfo.append(0)

    buttonInfo.append(button[button.index('>') + 2:].split(', '))

    buttonInfo.append(ind)
    ind += 1

    buttonInfo.append({})

    buttonDict[listOfKeys[-1]] = buttonInfo

for button in buttons:
    if button[0:button.index(' ')] == 'broadcaster':
        startIns = button[button.index(' ') + 4:].split(', ')
        continue
    
    buttonInfo = []
    if button[0] == '&': continue
    
    listOfKeys.append(button[1:button.index(' ')])

    buttonInfo.append(1)

    buttonInfo.append(button[button.index('>') + 2:].split(', '))

    for outputButton in buttonInfo[1]:
        if outputButton in buttonDict.keys() and buttonDict[outputButton][0] == 0:
            buttonDict[outputButton][3][button[1:button.index(' ')]] = 0

    buttonInfo.append(ind)
    ind += 1

    buttonDict[listOfKeys[-1]] = buttonInfo

listOfConjunction = []

for i, button in enumerate(listOfKeys):
    if buttonDict[button][0] == 1: listOfConjunction.append(i)

inputsOn = {'tx': [], 'dd':[], 'nz':[], 'ph':[]}
currState = [0 for _ in range(len(listOfKeys))]
steps = 0
while True:
    queue = [[key, 0, ''] for key in startIns]
    lowSent = len(queue) + 1
    highSent = 0

    rxLow = 0

    while len(queue) > 0:
        currButton, pulseStrength, sender = queue.pop(0)
        if currButton == 'rx' and pulseStrength == 0: rxLow += 1
        if currButton not in buttonDict.keys(): continue
        buttonInfo = buttonDict[currButton]
        if buttonInfo[0] == 1:
            if pulseStrength == 0:
                currState[buttonInfo[2]] = (currState[buttonInfo[2]] + 1) % 2
                if currState[buttonInfo[2]] == 0: lowSent += len(buttonInfo[1])
                else: highSent += len(buttonInfo[1])
                for outputSignal in buttonInfo[1]: queue.append([outputSignal, currState[buttonInfo[2]], currButton])
        else:
            buttonDict[currButton][3][sender] = pulseStrength
            buttonInfo = buttonDict[currButton]
            if sum(list(buttonInfo[3].values())) == len(list(buttonInfo[3].values())):
                for outputSignal in buttonInfo[1]: queue.append([outputSignal, 0, currButton])
                lowSent += len(buttonInfo[1])
            else:
                for outputSignal in buttonInfo[1]: queue.append([outputSignal, 1, currButton])
                highSent += len(buttonInfo[1])
                if currButton in inputsOn.keys() and len(inputsOn[currButton]) < 5: inputsOn[currButton].append(steps + 1)
            
            if sum(list(buttonInfo[3].values())) == 0: currState[buttonInfo[2]] = 0
            else: currState[buttonInfo[2]] = 1

    steps += 1
    if rxLow == 1: break
    
    allGood = True
    for arr in inputsOn.values():
        if len(arr) < 5: allGood = False
    
    if allGood: break

for arr in inputsOn.values(): print(arr)

