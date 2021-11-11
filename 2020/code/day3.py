# Day 3 code
def read_input(file):
    a = []
    with open(file,'r') as F:
        a = F.readlines()
    return a

def proc1(a,R=3,D=1):
    right,down = (R,D)
    cur_pos = 0
    tr_cnt = 0
    i = down
    while i < len(a):
        cur_pos = cur_pos + right
        if a[i][cur_pos % len(a[i])] == '#':
            tr_cnt += 1
        i += down
    return tr_cnt

def part1():
    file = "../input/day3.txt"
    a = read_input(file)
    a = [ii.strip('\n') for ii in a]
    t = proc1(a,R=3,D=1)
    print("Number of trees: ",t)
    
def part2():
    file = "../input/day3.txt"
    a = read_input(file)
    a = [ii.strip('\n') for ii in a]
    t = 1
    cb = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for ii in cb:
        p = proc1(a,R=ii[0],D=ii[1])
        print("Trees",p)
        t *= p 
    print("Number of trees: ",t)

def main():
    #part1()
    part2()

if __name__ == "__main__":
    main()