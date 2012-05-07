from itertools import izip
from collections import defaultdict

def match_len(x, y):
    l = 0

    for a, b in izip(x, y):
        if a != b:
            break
        l += 1

    return l

def naive_self_sim(x):
    similarities = [match_len(x, x[i:]) for i in xrange(1, len(x))]
    return len(x) + sum(similarities)

def ultra_naive(x):
    total = len(x)

    for i in range(1, len(x)):
        for j in range(i, len(x)):
            if x[i] == x[j]:
                total += 1
            else:
                break

    return total

def quad_self_sim(x):
    '''O(n**2) worst case'''
    matched = [[i for i, a in enumerate(x) if a == x[0]]]
    cumsum = len(matched[0])

    for s in x[1:]:
        matched.append([i+1 for i in matched[0]
                        if i < len(x) - 1 and x[i+1] == s])
        matched.pop(0)
        cumsum += len(matched[0])

    return cumsum

def z_algo(s):
    zval = [len(s)] * len(s)
    l = r = -1

    for pos in xrange(1, len(s)):
        if pos <= r:
            # within interval

            if zval[pos-l] + pos <= r:
                # completely within interval
                zval[pos] = zval[pos-l]
            else:
                # similarity *may* extend beyond interval,
                # so we need to compare

                zval[pos] = r - pos + match_len(s[r-pos:], s[r:])
                l = pos
                r = l + zval[pos] - 1
        else:
            # outside interval, so compare and rebuild frame
            zval[pos] = match_len(s, s[pos:])

            if zval[pos] > 0:
                l = pos
                r = l + zval[pos] - 1
            else:
                l = r = -1

    return zval

def naive_z_algo(s):
    return [len(s)] + [match_len(s, s[i:]) for i in xrange(1, len(s))]

def linear_self_sim(s):
    return sum(z_algo(s))

if __name__ == "__main__":
    from sys import stdin, argv
    from pprint import pprint

    stdin.readline()

    for testcase in stdin:
        print linear_self_sim(testcase.strip())

    '''from util import rand_str

    print z_algo(argv[1])
    print naive_z_algo(argv[1])'''
