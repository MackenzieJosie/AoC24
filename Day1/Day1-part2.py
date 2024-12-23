# Opening file parsing the input and removing last empty line
input = open("input.txt").read().split("\n")
input.pop()

left, right = [], []

for i in range(len(input)):
    newLeft, newRight = input[i].split("   ")
    left.append(int(newLeft))
    right.append(int(newRight))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    total += left[i] * right.count(left[i])

print(total)