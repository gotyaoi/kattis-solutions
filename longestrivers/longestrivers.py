import sys
from heapq import heappush, heappop
def main():
    numrivers, numconfluences = [int(x) for x in input().split()]
    data = sys.stdin.read().splitlines()
    #points contains confluences first, then rivers
    points = [(int(conf)-1, int(dist))
              for conf, dist
              in [line.split()
                  for line
                  in data[numrivers:]]]
    rivernames = []
    for name, conf, dist in [line.split() for line in data[:numrivers]]:
        rivernames.append(name)
        points.append((int(conf)-1, int(dist)))
    #upstream contains all upstream points for each confluence
    upstream = [[] for _ in range(numconfluences)]
    to_check = []
    for i, (conf, dist) in enumerate(points):
        if conf != -1:
            upstream[conf].append((i, dist))
        else:
            to_check.append((i, dist))
    #max_len contains the best case length for each river, along with the river's index
    max_len = [0]*numrivers
    while to_check:
        i, dist = to_check.pop()
        if i >= numconfluences:
            max_len[i-numconfluences] = (dist, i-numconfluences)
        else:
            to_check.extend([(x, dist+d) for x, d in upstream[i]])
    #state1 implicitely contains all confluences at the start
    #state2 is all rivers which are long and all confluences with short upstreams but which turn long
    state2 = []
    #state3 is all rivers which are short and all confluences with short upstreams and which stay short
    state3 = set()
    #lengths is the length of each upstream point for each confluence
    lengths = [[] for _ in range(numconfluences)]
    ranks = [0]*numrivers
    for i, (conf, dist) in enumerate(points[numconfluences:], start=numconfluences):
        heappush(state2, (dist, i))
    for length, riverindex in sorted(max_len):
        try:
            priority, index = heappop(state2)
            while priority <= length:
                state3.add(index)
                downstreamindex = points[index][0]
                if downstreamindex != -1:
                    lengths[downstreamindex].append(priority)
                    conf = points[downstreamindex]
                    ups = upstream[downstreamindex]
                    if all([x[0] in state3 for x in ups]):
                        conflen = min([x for x in lengths[downstreamindex]]) + conf[1]
                        if conflen <= length:
                            index = downstreamindex
                            priority = conflen
                            continue
                        else:
                            heappush(state2, (conflen, downstreamindex))
                priority, index = heappop(state2)
            heappush(state2, (priority, index))
        except IndexError:
            #state2 is empty
            pass
        ranks[riverindex] = len(state2) + 1
    for i, name in enumerate(rivernames):
        print(name, ranks[i])
main()
