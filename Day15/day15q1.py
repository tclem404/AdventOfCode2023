import fileinput

codes = list(fileinput.input(files=['Day15/val.txt']))[0].replace('\n','').split(',')

total = 0
for currCode in codes:
    inputLens = list(currCode)
    hashVal = 0
    for character in inputLens:
        hashVal += ord(character)
        hashVal *= 17
        hashVal %= 256
    total += hashVal
    
print(total)
