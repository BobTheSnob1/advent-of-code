import re

sum = 0

with open('1.in', 'r') as file:
    data = file.read()
    working = 1
    # what the fuck is a "non-capturing group"???? shrug
    pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)|(?:do\(\)|don\'t\(\))'
    instructions = re.findall(pattern, data)
    for instruction in instructions:
        if instruction == "do()":
            working = 1
        elif instruction == "don't()":
            working = 0
        else:
            if working:
                operands = re.findall(r'[0-9]{1,3}', instruction)
                sum += int(operands[0]) * int(operands[1])

print(sum)
