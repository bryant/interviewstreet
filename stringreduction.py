'''
Each query runs at O(n), n proportional to length of input string,
but hell, that's practically O(1) for n < 10**4. Total runtime for
the problem is O(num of queries), then. Neat.
'''

def char_freq_3(s):
    '''Returns character frequency of string s. Relies on every char
    of s being 0x61, 0x62, or 0x63; this is a mega-hack to speed
    things up.
    '''

    freq = [0] * 3

    for c in s:
        freq[ord(c) - 0x61] += 1

    return freq

def reduced_len(freq):
    '''Proposition 1:
    The character frequency of string s is either:
    - All odd
    - All even
    - All repeats (0, 0, n) or (0, n, 0) or (n, 0, 0)
    - 2 odd, 1 even / 2 even 1 odd

    in which case the shortest reduction has length, respectively:
    - 2
    - 2
    - n
    - 1

    Proof:
    Case 3 is obvious. For the other cases, take note that every round
    of reduction reverses the parity of all 3 freqs. So all odd becomes
    all even, all even becomes all odd, etc. No room in margin of this
    vim to prove the rest. Just ponder.
    '''

    freq.sort()

    # case 0: original string is aaaa, bbb, ccc
    if freq[0] == freq[1] == 0:
        return freq[2]

    if is_even(freq[0] + freq[1]) and is_even(freq[1] + freq[2]):
        # case 1: all 3 freqs are all even or all odd
        return 2

    return 1


is_even = lambda n: (n % 2) == 0

if __name__ == "__main__":
    from sys import stdin

    stdin.readline()

    for line in stdin:
        print reduced_len(char_freq_3(line.strip()))
