def main():
    e = iter(sorted([int(x) for x in input().split()[1:]]))
    m = iter(sorted([int(x) for x in input().split()[1:]]))
    for next_e in e:
        break
    else:
        next_e = None
    for next_m in m:
        break
    else:
        next_m = None
    for count in range(1000001):
        if next_e is None or next_m is None:
            break
        if next_e < next_m:
            for next_e in e:
                if next_e >= next_m:
                    break
            else:
                next_e = None
        elif next_m < next_e:
            for next_m in m:
                if next_m >= next_e:
                    break
            else:
                next_m = None
        else:
            for next_e in e:
                break
            else:
                next_e = None
            for next_m in m:
                break
            else:
                next_m = None
    if next_e is not None or next_m is not None:
        count += 1
    print(count)
main()
