import sys
def main():
    for i, line in enumerate(sys.stdin, start=1):
        s = sorted([int(x) for x in line.split()[1:]])
        print('Case {}: {} {} {}'.format(i, s[0], s[-1], s[-1]-s[0]))
main()
