import sys
def main():
    numcities = int(input())
    cities = sys.stdin.readlines()
    index = 0
    for _ in range(numcities):
        unvisited = set(range(int(cities[index])))
        numconnections = int(cities[index+1])
        connections = {x: [] for x in unvisited}
        for x, y in [[int(x) for x in conn.split()] for conn in cities[index+2:index+2+numconnections]]:
            connections[x].append(y)
            connections[y].append(x)
        adds = -1
        while unvisited:
            adds += 1
            to_check = [unvisited.pop()]
            while to_check:
                hub = to_check.pop()
                for endpoint in connections[hub]:
                    if endpoint in unvisited:
                        unvisited.remove(endpoint)
                        to_check.append(endpoint)
        print(adds)
        index += 2+numconnections
main()
