import sys
def prime_factors(n):
    i = 2
    factors = []
    s = []
    while i * i <= n:
        if n % i:
            i += 1
            if s:
                factors.append(s)
                s = []
        else:
            n //= i
            s.append(i)
    if s:
        factors.append(s)
    if n > 1:
        if n == i and factors:
            factors[-1].append(n)
        else:
            factors.append([n])
    return factors
def main():
    lines = [x[:-1] for x in sys.stdin.readlines()[:-1]]
    for line in lines:
        linelen = len(line)
        pf = prime_factors(linelen)
        if not pf:
            pf = [[linelen]]
        best = 1
        for factors in pf:
            for numparts in factors:
                numparts = best*numparts
                partlen = linelen//numparts
                if line[:partlen]*numparts == line:
                    best = numparts
                else:
                    break
        print(best)
main()
