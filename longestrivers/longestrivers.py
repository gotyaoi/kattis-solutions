import sys
from heapq import heapify, heappush, heappop
def main():
    numrivers, numconfluences = [int(x) for x in input().split()]
    data = sys.stdin.read().splitlines()
    #points contains confluences first, then rivers
    points = [(int(dist), int(conf)-1)
              for conf, dist
              in [line.split()
                  for line
                  in data[numrivers:]]]
    rivernames = []
    for name, conf, dist in [line.split() for line in data[:numrivers]]:
        rivernames.append(name)
        points.append((int(dist), int(conf)-1))
    #upstream contains all upstream points for each confluence
    upstream = [[] for _ in range(numconfluences)]
    to_check = []
    for i, (dist, conf) in enumerate(points):
        if conf != -1:
            upstream[conf].append((i, dist))
        else:
            to_check.append((i, dist))
    #max_len contains the best case length for each river, along with the river's index
    max_len = [None]*numrivers
    try:
        while True:
            i, dist = to_check.pop()
            if i >= numconfluences:
                max_len[i-numconfluences] = (dist, i-numconfluences)
            else:
                to_check.extend([(x, dist+d) for x, d in upstream[i]])
    except IndexError:
        pass
    max_len.sort()
    #state1 implicitely contains all confluences at the start
    #state2 is all rivers which are long and all confluences with short upstreams but which turn long
    state2 = points[numconfluences:]
    heapify(state2)
    #state3 implicitely contains all rivers which are short and all confluences with short upstreams and which stay short
    #lengths is the length of each upstream point for each confluence
    lengths = [[] for _ in range(numconfluences)]
    ranks = [1]*numrivers
    priority, downstreamindex = heappop(state2)
    try:
        for length, riverindex in max_len:
            while priority <= length:
                #index goes to state3
                if downstreamindex != -1:
                    lengths[downstreamindex].append(priority)
                    if len(upstream[downstreamindex]) == len(lengths[downstreamindex]):
                        p_dist, p_conf = points[downstreamindex]
                        conflen = min([x for x in lengths[downstreamindex]]) + p_dist
                        if conflen <= length:
                            downstreamindex = p_conf
                            priority = conflen
                            continue
                        else:
                            heappush(state2, (conflen, p_conf))
                priority, downstreamindex = heappop(state2)
            ranks[riverindex] = len(state2) + 2
    except IndexError:
        #state2 is empty
        pass
    for name, rank in zip(rivernames, ranks):
        print(name, rank)
main()
