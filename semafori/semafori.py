import sys
def main():
    numlights, length = [int(x) for x in input().split()]
    lights = [[int(x) for x in line.split()] for line in sys.stdin]
    time = 0
    prev_distance = 0
    for distance, red, green in lights:
        time += (distance-prev_distance)
        prev_distance = distance
        rem = time % (red+green)
        if rem < red:
            time += (red-rem)
    print(time+length-distance)
main()
