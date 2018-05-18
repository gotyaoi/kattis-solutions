import sys
def main():
    rows, columns = [int(x) for x in input().split()]
    table = sorted(zip(*reversed([x.strip() for x in sys.stdin.readlines()])))
    low = 0
    high = rows - 1
    best = 0
    while low <= high:
        i = (low + high) // 2
        comp = rows - i
        if all(a[:comp] != b[:comp] for a, b in zip(table[:columns-1], table[1:columns])):
            best = i
            low = i + 1
        else:
            high = i - 1
    print(best)
main()
