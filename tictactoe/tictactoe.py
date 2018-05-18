import sys
from collections import Counter
def main():
    numboards = int(input())
    boards = sys.stdin.read()
    start = 0
    for i in range(numboards):
        board = boards[start:start+11]
        counts = Counter(board)
        tl, tm, tr = board[0:3]
        ml, mm, mr = board[4:7]
        bl, bm, br = board[8:11]
        # [top, left, bottom, right, vert, horiz, back, slash]
        xwin = [0, 0, 0, 0, 0, 0, 0, 0]
        owin = [0, 0, 0, 0, 0, 0, 0, 0]
        if tl==tm==tr=='X':
            xwin[0] = 1
        if tl==tm==tr=='O':
            owin[0] = 1
        if tl==ml==bl=='X':
            xwin[1] = 1
        if tl==ml==bl=='O':
            owin[1] = 1
        if bl==bm==br=='X':
            xwin[2] = 1
        if bl==bm==br=='O':
            owin[2] = 1
        if tr==mr==br=='X':
            xwin[3] = 1
        if tr==mr==br=='O':
            owin[3] = 1
        if tm==mm==bm=='X':
            xwin[4] = 1
        if tm==mm==bm=='O':
            owin[4] = 1
        if ml==mm==mr=='X':
            xwin[5] = 1
        if ml==mm==mr=='O':
            owin[5] = 1
        if tl==mm==br=='X':
            xwin[6] = 1
        if tl==mm==br=='O':
            owin[6] = 1
        if tr==mm==bl=='X':
            xwin[7] = 1
        if tr==mm==bl=='O':
            owin[7] = 1
        xwins = sum(xwin)
        owins = sum(owin)
        if xwin[0] and xwin[1]:
            xwins -= 1
        elif xwin[1] and xwin[2]:
            xwins -= 1
        elif xwin[2] and xwin[3]:
            xwins -= 1
        elif xwin[3] and xwin[1]:
            xwins -= 1
        if xwin[4] and xwin[5]:
            xwins -= 1
        if xwin[6] and xwin[7]:
            xwins -= 1
        if owin[0] and owin[1]:
            owins -= 1
        elif owin[1] and owin[2]:
            owins -= 1
        elif owin[2] and owin[3]:
            owins -= 1
        elif owin[3] and owin[1]:
            owins -= 1
        if owin[4] and owin[5]:
            owins -= 1
        if owin[6] and owin[7]:
            owins -= 1
        if xwins + owins > 1:
            print('no')
        elif xwins == 1 and counts['X']-1 == counts['O']:
            print('yes')
        elif owins == 1 and counts['X'] == counts['O']:
            print('yes')
        elif xwins == 0 and owins == 0 and (counts['X']-1 == counts['O'] or counts['X'] == counts['O']):
            print('yes')
        else:
            print('no')
        start += 13
main() 
