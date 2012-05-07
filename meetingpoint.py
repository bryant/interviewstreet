def travel(a, b):
   return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def avg(points):
    adder = lambda x, y: (x[0]+y[0], x[1]+y[1])
    s = reduce(adder, points)
    n = len(points)
    return (s[0]/n, s[1]/n)

def n_closest_to(p, points, n=4):
    #mindist, bestp = min((travel(p, k), k) for k in points)
    bestp = sorted((travel(p, k), k) for k in points)[:n]
    return [p for _, p in bestp]

def total_travel_to(p, points):
    #return sum(map(travel, points, [p]*len(points)))
    return sum(travel(p, i) for i in points)

def naive(points):
    return min(total_travel_to(p, points) for p in points)

if __name__ == "__main__":
    from sys import stdin
    import re

    linereader = re.compile(r"(^[-+]?\d+) ([-+]?\d+)$", re.MULTILINE)

    size = int(stdin.readline())
    homes = [(int(x), int(y)) \
             for x, y in linereader.findall(stdin.read())]

    centers = n_closest_to(avg(homes), homes)
    print min(total_travel_to(center, homes) for center in centers)
