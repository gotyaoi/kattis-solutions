import sys
def main():
    lines = sys.stdin.readlines()
    i = 1
    guess = int(lines[0])
    highs = []
    lows = []
    while guess > 0:
        response = lines[i]
        i += 1
        if response == 'too high\n':
            highs.append(guess)
        elif response == 'too low\n':
            lows.append(guess)
        else:
            dishonest = False
            for high in highs:
                if high <= guess:
                    dishonest = True
                    break
            if not dishonest:
                for low in lows:
                    if low >= guess:
                        dishonest = True
                        break
            if dishonest:
                print('Stan is dishonest')
            else:
                print('Stan may be honest')
            highs.clear()
            lows.clear()
        guess = int(lines[i])
        i += 1
main()
