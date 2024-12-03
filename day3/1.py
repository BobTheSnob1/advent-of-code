import re

sum = 0

with open('1.in', 'r') as file:
    data = file.read()
    for mul in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data):
        operands = re.findall(r'[0-9]{1,3}', mul)
        sum += int(operands[0]) * int(operands[1])

print(sum)
