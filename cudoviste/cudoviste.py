import sys
def main():
    R, C = [int(x) for x in sys.stdin.readline().split()]
    map = sys.stdin.read().split()
    groups = [0, 0, 0, 0, 0]
    for r in range(R-1):
        for c in range(C-1):
            cars = 0
            for roff, coff in [(r,c), (r,c+1), (r+1,c), (r+1,c+1)]:
                space = map[roff][coff]
                if space == '#':
                    break
                elif space == 'X':
                    cars += 1
            if space != '#':
                groups[cars] += 1
    print(groups[0], groups[1], groups[2], groups[3], groups[4], sep='\n')
main()
