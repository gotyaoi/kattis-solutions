def main():
    x = int(input()) > 0
    y = int(input()) > 0
    if x:
        if y:
            print('1')
        else:
            print('4')
    else:
        if y:
            print('2')
        else:
            print('3')
main()
