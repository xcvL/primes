from math import isqrt
from typing import List

def _simple_primes_up_to(n: int) -> List[int]:
    '''
    Helper: sieve primes up to n (inclusive) - used to get base primes for segmented sieve
    '''
    if n < 2:
        return []
    sieve = bytearray(n + 1)
    sieve[0:2] = b"\x01\x01"
    lim = isqrt(n)
    for p in range(2, lim + 1):
        if sieve[p] == 0:
            step = p
            start = p * p
            sieve[start:n+1:step] = b"\x01" * ((n - start) // step + 1)
    return [i for i in range(2, n + 1) if sieve[i] == 0]

def _primes_in_range_segmented(a: int, b: int) -> List[int]:
    '''
    Segmented sieve: returns primes p with a <= p < b.

    Efficient when b is large but (b-a) is manageable.

    Works for very large b (e.g. up to 1e12), limited by memory for the segment size (b-a).
    '''
    if b <= 2:
        return []
    if a < 2:
        a = 2
    # base primes up to sqrt(b-1)
    limit = isqrt(b - 1)
    base_primes = _simple_primes_up_to(limit)
    segment_size = b - a
    seg = bytearray(segment_size) # 0: possibly prime, 1: composite

    for p in base_primes:
        # first multiple of p in [a, b)
        start = (a + p - 1) // p * p
        if start < p * p:
            start = p * p
        # mark multiples
        offset = start - a
        step = p
        seg[offset:segment_size:step] = b"\x01" * ((segment_size - 1 - offset) // step + 1)
    
    return [a + i for i in range(segment_size) if seg[i] == 0]