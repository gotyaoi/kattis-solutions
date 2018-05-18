import sys
def main():
    books = int(input())
    prices = [int(x) for x in sys.stdin.read().split()]
    prices.sort(reverse=True)
    print(sum(prices[0::3])+sum(prices[1::3]))
main()
