import sys
from itertools import zip_longest
def main():
    prices = sorted([int(x) for x in sys.stdin.readlines()[1:]], reverse=True)
    walkers = [iter(prices)] * 3
    total = 0
    for a, b, _ in zip_longest(*walkers, fillvalue=0):
        total += a+b
    print(total)
main()
