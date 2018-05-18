import sys
def main():
    data = sys.stdin.readlines()
    start = 1
    rows = int(data[0].split()[0])
    while rows > 0:
        print('\n'.join([''.join(x) for x in zip(*sorted(zip(*[x.strip() for x in data[start:start+rows]]), key=lambda x: [y.lower() for y in x]))]))
        start += rows
        rows = int(data[start].split()[0])
        start += 1
        if rows > 0:
            print()
main()
