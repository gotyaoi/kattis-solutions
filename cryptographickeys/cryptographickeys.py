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
    num = int(input())
    smallest_zeros = 0
    smallest_base = 0
    for base in prime_factors(num):
        if base > num:
            break
        zeros = 0
        quot = num
        rem = 0
        while True:
            quot, rem = divmod(quot, base)
            if rem == 0:
                zeros += 1
            else:
                break
        if zeros > smallest_zeros:
            smallest_zeros = zeros
            smallest_base = base
    print(smallest_base)
main()
