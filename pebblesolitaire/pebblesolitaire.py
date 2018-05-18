import sys
def main():
    numpuzzles = int(input())
    puzzles = [[1 if x == 'o' else 0 for x in line.strip()] for line in sys.stdin.readlines()]
    for puzzle in puzzles:
        start = sum(puzzle)
        nextstates = []
        for i in range(len(puzzle)-2):
            segment = puzzle[i:i+3]
            if segment == [1, 1, 0]:
                nextstates.append(puzzle[:])
                nextstates[-1][i:i+3] = [0, 0, 1]
            elif segment == [0, 1, 1]:
                nextstates.append(puzzle[:])
                nextstates[-1][i:i+3] = [1, 0, 0]
        moves = 0
        while nextstates:
            moves += 1
            nextnextstates = []
            for state in nextstates:
                for i in range(len(state)-2):
                    segment = state[i:i+3]
                    if segment == [1, 1, 0]:
                        nextnextstates.append(state[:])
                        nextnextstates[-1][i:i+3] = [0, 0, 1]
                    elif segment == [0, 1, 1]:
                        nextnextstates.append(state[:])
                        nextnextstates[-1][i:i+3] = [1, 0, 0]
            nextstates = nextnextstates
        print(start-moves)
main()
