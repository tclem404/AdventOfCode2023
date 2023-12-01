import fileinput

sum = 0
for line in fileinput.input(files=['Day1/val.txt']):
    line = line.lower()
    line = line.replace('one','one1one')
    line = line.replace('two','two2two')
    line = line.replace('three','three3three')
    line = line.replace('four','four4four')
    line = line.replace('five','five5five')
    line = line.replace('six','six6six')
    line = line.replace('seven','seven7sevenn')
    line = line.replace('eight','eight8eightt')
    line = line.replace('nine','nine9nine')
    nums = [int(i) for i in line if i.isdigit()]
    sum += 10*nums[0] + nums[-1]

print(sum)