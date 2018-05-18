def main():
    numkeys, pressed = [int(x) for x in input().split()]
    keys = sorted([int(x) for x in input().split()])
    incidence_len = numkeys-pressed+1
    incidence = [1]*incidence_len
    total = 1
    for n, k in zip(range(pressed, numkeys), range(1, incidence_len)):
        total = total*n//k
        incidence[k] = total
    print(sum([x*y for x, y in zip(keys[pressed-1:], incidence)])%1000000007)
main()
