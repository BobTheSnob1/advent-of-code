a = []
b = []

line = input()

while line != '':
    line = line.split('   ')
    a.append(line[0])
    b.append(line[1])
    line = input()

a.sort()
b.sort()

distance = 0

for _ in range(len(a)):
    distance += abs(int(a[_]) - int(b[_]))

print(distance)
