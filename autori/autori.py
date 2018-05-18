def main():
    line = input()
    print(''.join([x[0] for x in line.split('-')]))
main()
