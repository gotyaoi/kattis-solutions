def main():
    shift = int(input())
    while shift > 0:
        plain = ''.join(input().upper().split())
        lp = len(plain)
        cipher = [None]*lp
        cs = 0
        ci = 0
        for c in plain:
            if ci < lp:
                cipher[ci] = c
                ci += shift
            else:
                cs += 1
                cipher[cs] = c
                ci = cs + shift
        print(''.join(cipher))
        shift = int(input())
main()
