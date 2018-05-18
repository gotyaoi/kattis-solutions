def main():
    numstudents, numinstructions = [int(x) for x in input().split()]
    instructions = input().split()
    reduced = []
    i = 0
    l = len(instructions)
    while i < l:
        try:
            reduced.append(int(instructions[i]))
        except ValueError:
            i += 1
            back = -1*int(instructions[i])
            reduced = reduced[:back]
        i += 1
    print(sum(reduced)%numstudents)
main()
