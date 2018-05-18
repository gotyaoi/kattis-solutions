import sys
def main():
    houses, _ = [int(x) for x in input().split()]
    connections = [[] for _ in range(houses+1)]
    for x, y in [[int(y) for y in x.split()] for x in sys.stdin]:
        connections[x].append(y)
        connections[y].append(x)
    connected = [False for _ in range(houses+1)]
    connected[1] = True
    to_check = list(connections[1])
    while to_check:
        t = to_check.pop()
        if not connected[t]:
            connected[t] = True
            for t2 in connections[t]:
                to_check.append(t2)
    unconnected = [x for x in range(2, houses+1) if not connected[x]]
    if not unconnected:
        print('Connected')
    else:
        for x in unconnected:
            print(x)
main()
