def main():
    a = input().split()
    b = [x for x in a if 'ae' in x]
    if len(b)/len(a) >= .4:
        print('dae ae ju traeligt va')
    else:
        print('haer talar vi rikssvenska')
main()
