# Day4 code
import sys 

def read_input(file):
    a = []
    with open(file,'r') as F:
        a = F.readlines()
    if a:
        aa = []
        d  = ""
        for i in a:
            if i == '\n':
                if d:
                    aa.append(d)
                    d = ""
            else:
                d += i + " "
        aa = [line.replace('\n',"") for line in aa]
    return aa

def part1():
    file = "../input/day4.txt"
    a = read_input(file)
    ids = [
        'byr:', 
        'iyr:',
        'eyr:',
        'hgt:',
        'hcl:',
        'ecl:',
        'pid:'
        #'cid:'
    ]
    pc = 0
    for i in a:
        valid = True
        for ii in ids:
            if ii not in i:
                valid = False
                break
        if valid:
            pc += 1
    print("Num valid passports",pc)

def part2():
    file = "../input/day4.txt"
    a = read_input(file)
    ids = [
        'byr:', 
        'iyr:',
        'eyr:',
        'hgt:',
        'hcl:',
        'ecl:',
        'pid:'
        #'cid:'
    ]
    pc = 0
    for i in a:
        valid = True
        for ii in ids:
            if ii not in i:
                valid = False
                break
            elif ii == 'byr:':
                yr = (i.split(ii)[-1].split()[0])
                if int(yr) < 1920 or int(yr) > 2002 or len(yr) != 4:
                    valid = False
                    break
            elif ii == 'iyr:':
                yr = (i.split(ii)[-1].split()[0])
                if int(yr) < 2010 or int(yr) > 2020 or len(yr) != 4:
                    valid = False
                    break
            elif ii == 'eyr:':
                yr = (i.split(ii)[-1].split()[0])
                if int(yr) < 2020 or int(yr) > 2030 or len(yr) != 4:
                    valid = False
                    break
            elif ii == 'hgt:':
                yr = i.split(ii)[-1].split()[0]
                if 'cm' in yr: 
                    hh = int(yr.split('cm')[0])
                    if hh < 150 or hh > 193:
                        valid = False
                        break
                elif 'in' in yr:
                    hh = int(yr.split('in')[0])
                    if hh < 59 or hh > 76:
                        valid = False
                        break
                else:
                    valid = False
                    break
            elif ii == 'hcl:':
                yr = i.split(ii)[-1].split()[0]
                if '#' == yr[0] and len(yr) == 7:
                    rm = yr[1:]
                    if rm.isalnum():
                        for it in rm:
                            if it.isnumeric():
                                continue
                            elif it in ['a','b','c','d','e','f']:
                                continue
                            else:
                                valid = False
                                break
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
            elif ii == 'ecl:':
                yr = i.split(ii)[-1].split()[0]
                if yr not in ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid = False
                    break
            elif ii == 'pid:':
                yr = i.split(ii)[-1].split()[0]
                if not(len(yr) == 9 and yr.isnumeric()):
                    valid = False
                    break
        if valid:
            print(i)
            pc += 1
    print("Num valid passports",pc)


def main():
    #part1()
    part2()

if __name__ == "__main__":
    main()