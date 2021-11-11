# Day 2 solution

def read_input(file):
    a = []
    with open(file,'r') as F:
        a = F.readlines()
    return a

def proc(a):
    count = 0
    for i in a:
        d = i.split()
        fr = d[0].split('-')
        fr_low = int(fr[0])
        fr_high= int(fr[-1])
        letter = d[1][0]
        passwd = d[-1]
        lcount = passwd.count(letter)
        if lcount >= fr_low and lcount <= fr_high:
            count += 1
    return count

def proc2(a):
    count = 0
    for i in a:
        d = i.split()
        fr = d[0].split('-')
        pos1 = int(fr[0])
        pos2 = int(fr[-1])
        letter = d[1][0]
        passwd = d[-1]
        if (passwd[pos1-1] == letter and passwd[pos2-1] != letter) or (passwd[pos1-1] != letter and passwd[pos2-1] == letter):
            count += 1    
    return count

def part2():
    file = "../input/day2.txt"
    a = read_input(file)
    a = [ii.strip('\n') for ii in a]
    c = proc2(a)
    print("#valid:",c)

def part1():
    file = "../input/day2.txt"
    a = read_input(file)
    a = [ii.strip('\n') for ii in a]
    c = proc(a)
    print("#valid:",c)

def main():
    #part1()
    part2()

if __name__ == "__main__":
    main()