from re import findall

def part1():
    d = open("input.txt").read()
    print(sum(int(x)*int(y) for x,y in findall(r"mul\((\d+),(\d+)\)", d)))

def part2():
    d = "do()" + open("input.txt").read().replace('\n',' ') + "don't()"
    d = "".join(findall(r"do\(\)(.*?)don't\(\)", d))
    print(sum(int(x)*int(y) for x,y in findall(r"mul\((\d+),(\d+)\)", d)))

part1()
part2()

