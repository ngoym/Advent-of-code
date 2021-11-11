import os

def read_input(file):
    a = []
    with open(file,'r') as F:
        a = F.readlines()
    return a

def part1():
    file = "../input/day1a.txt"
    a = read_input(file)
    a = [int(ii.strip('\n')) for ii in a]

    for i in range(len(a)):
        diff = 2020 - a[i]
        if diff in a:
            pr = diff * a[i]
            num = a[i]
            break
    print("prod:",pr)
    print((num, diff))

def part2_help(target, a):
    pr = -1
    num = -1
    for i in range(len(a)):
        diff = target - a[i]
        if diff in a:
            pr = diff * a[i]
            num = a[i]
            break
    return pr, num, diff

def part2():
    file = "../input/day1a.txt"
    a = read_input(file)
    a = [int(ii.strip('\n')) for ii in a]
    sa = sorted(a)
    for ii in sa:
        p,n,d = part2_help(2020-ii, a)
        if p != -1:
            print("Nums:", ii,n,d)
            print("Prod:",ii*n*d)
            break

def main():
    part2()
if __name__ == "__main__":
    main()