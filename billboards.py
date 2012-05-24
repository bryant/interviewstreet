def min_cost_recursive(billboards, maxgap):
    '''Reference naive solution. Given a seq, at least one of
    the last maxgap entries will be taken off. This method tests
    each of those entries and recurses upon itself.
    '''

    if len(billboards) <= maxgap:
        cost = 0
    else:
        candidates = (billboards[i] +
                      min_cost_recursive(billboards[i+1:], maxgap)
                      for i in xrange(maxgap+1))
        cost = min(candidates)
    return cost

def min_cost_dp(billboards, maxgap):
    '''Dynamic programming version of recursive.'''

    if len(billboards) <= maxgap:
        return 0

    mincosts = [0] * (len(billboards)+1)

    for i in xrange(maxgap, len(billboards)):
        expectedcosts = [billboards[i-j] + mincosts[i-j]
                         for j in xrange(maxgap+1)]
        mincosts[i+1] = min(expectedcosts)

    return mincosts[-1]

def min_cost_on(billboards, maxgap):
    '''Dynamic programming version, but runs in O(len(billboards))
    instead of O(len*maxgap). How? Notice in min_cost_dp that every
    new iteration of i only shifts expectedcosts over by 1. So we can
    replace the O(maxgap) min operation to O(1ish) on avg.
    '''

    def reverse_min(list_):
        '''finds the min with preference for latest occuring duplicate.'''
        min_ = list_[-1]
        pos = len(list_) - 1

        for i in xrange(len(list_)-1, -1, -1):
            if list_[i] < min_:
                min_ = list_[i]
                pos = i

        return min_, pos

    if len(billboards) <= maxgap:
        return 0

    expectedcosts = [0] * (maxgap+1)
    mincost, skipmin = 0, 0

    for i in xrange(len(billboards)):
        expectedcosts.append(billboards[i]+mincost)
        expectedcosts.pop(0)

        if skipmin <= 0:
            mincost, skipmin = reverse_min(expectedcosts)
        else:
            skipmin -= 1

    return mincost

def test_dp(testcases):
    for billboard, k in testcases:
        recurs = min_cost_recursive(billboard, k)
        dp = min_cost_on(billboard, k)
        print dp, recurs
        assert dp == recurs

if __name__ == "__main__":
    from sys import stdin
    from random import randint

    '''test_dp([
        ((5, 6, 7, 8), 2),
        ((8, 7, 6, 5), 2),
        ((2, 3, 5, 11, 15, 2, 200), 6),
        ((1, 2, 3, 1, 6, 10), 2)
        ])'''

    '''randseq = lambda len_: [randint(1, 2**24-1) for i in xrange(len_)]
    args = randseq(10**5), 10**5-1

    print min_cost_on(*args)
    print min_cost_dp(*args)'''

    n, k = [int(i) for i in stdin.readline().split()]
    billboards = [int(i) for i in stdin]

    print sum(billboards) - min_cost_on(billboards, k)
