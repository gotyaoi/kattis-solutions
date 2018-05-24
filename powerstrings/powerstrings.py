import collections
import sys
from functools import reduce
from itertools import product
from operator import mul
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def main():
    lines = [x[:-1] for x in sys.stdin.readlines()[:-1]]
    for line in lines:
        linelen = len(line)
        pf = prime_factors(linelen)
        if pf:
            c = collections.Counter(pf)
            factors = sorted([reduce(mul, x) for x in product(*[[base**x for x in seq] for base, seq in zip(c.keys(), [range(x+1) for x in c.values()])])])
        else:
            factors = [1, linelen]
        for divisor in factors:
            quotient = linelen//divisor
            t = line[:divisor]*quotient
            if t == line:
                print(quotient)
                break
main()
