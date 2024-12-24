# Opening file parsing the input and removing last empty line
input = open("input.txt").read().split("\n")
input.pop()

def part1():
    total = 0
    for i in range(len(input)):
        line = input[i].split(" ")
        if int(line[0]) < int(line[1]):
            direction = 1
        else:
            direction = -1
        for j in range(len(line)-1):
            if int(line[j]) == int(line[j+1]):
                # print(line)
                break
            
            if int(line[j]) < int(line[j+1]) and direction == -1:
                # print(line)
                break

            if int(line[j]) > int(line[j+1]) and direction == 1:
                # print(line)
                break

            diff = abs(int(line[j]) - int(line[j+1]))
            if diff > 3:
                # print(line)
                break

            if j == len(line)-2:
                total += 1

    return total

def part2():
    total = 0
    for i in range(len(input)):
        originalLine = input[i].split(" ")
        safe = 0
        for b in range(len(originalLine)):
            line = list(originalLine)
            print(line)
            line.pop(b)
            if int(line[0]) < int(line[1]):
                direction = 1
            else:
                direction = -1
            for j in range(len(line)-1):
                if int(line[j]) == int(line[j+1]):
                    break
                
                if int(line[j]) < int(line[j+1]) and direction == -1:
                    break

                if int(line[j]) > int(line[j+1]) and direction == 1:
                    break

                diff = abs(int(line[j]) - int(line[j+1]))
                if diff > 3:
                    break

                if j == len(line)-2:
                    total += 1
                    safe = 1
            if safe == 1:
                break
    return total


print(part1())
print(part2())