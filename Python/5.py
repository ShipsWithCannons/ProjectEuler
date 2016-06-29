from primefac import gcd

def get_smallest_evenly_dividible():
    curr = 2520
    for i in xrange(11, 21):
        curr *= i / gcd(curr, i)
    return curr

print get_smallest_evenly_dividible()
