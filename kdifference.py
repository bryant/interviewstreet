'''Wondering if this could run faster than O(n)'''

if __name__ == "__main__":
    from sys import stdin

    n, k = [int(i) for i in stdin.readline().split()]
    count = 0
    # ordered = sorted(int(i) for i in stdin.readline().split())
    ints = set(int(i) for i in stdin.readline().split())

    for i in ints: # O(n)
        if (i + k) in ints: # O(1)
            count += 1

    print count
