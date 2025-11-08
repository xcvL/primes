import math

def segmented_sieve_range(a: int, b: int, segment_size: int = 100_000):
    """
    세그먼트화된 에라토스테네스의 체를 이용해 구간 [a, b)의 소수를 찾는 제너레이터.

    segment_size 단위로 나누어 처리.

    Parameters
    -------
    a: int
        구간 시작 (포함)
    b: int
        구간 끝 (제외)
    segment_size: int
        세그먼트 크기 (기본값 100,000)

    Yield
    -------
    yield: int
        구간 내의 소수
    """
    import math

    if b <= 2:
        return
    if a < 2:
        a = 2

    # √b 이하의 소수 구하기 (기본 체)
    limit = int(math.isqrt(b)) + 1
    base_sieve = bytearray(b'\x01') * (limit + 1)
    base_sieve[0:2] = b'\x00\x00'

    for i in range(2, limit + 1):
        if base_sieve[i]:
            base_sieve[i*i : limit + 1 : i] = b'\x00' * ((limit - i*i)//i + 1)

    base_primes = [i for i, is_prime in enumerate(base_sieve) if is_prime]

    # 세그먼트 단위로 [a, b) 처리
    low = a
    high = min(a + segment_size, b)

    while low < b:
        # 세그먼트 배열 초기화 (모두 True로 시작)
        segment = bytearray(b'\x01') * (high - low)

        for p in base_primes:
            # p*p보다 작은 구간에서는 p*p부터 시작
            start = max(p*p, ((low + p - 1)//p) * p)
            if start >= high:
                continue
            segment[start - low : high - low : p] = b'\x00' * ((high - start - 1)//p + 1)

        # 소수 yield
        for i, is_prime in enumerate(segment):
            if is_prime:
                yield low + i

        # 다음 세그먼트로 이동
        low = high
        high = min(high + segment_size, b)

def segmented_sieve_n(start: int, n: int, segment_size: int = 100_000):
    """
    a부터 시작해서 n개의 소수를 찾는 세그먼트화된 에라토스테네스의 체.

    segment_size 단위로 나누어 처리.

    Parameters
    -------
    start: int
        시작 숫자 (포함)
    n: int
        찾을 소수 개수
    segment_size: int
        세그먼트 크기 (기본값 100,000)
    Yield
    -------
    yield: int
        n개의 소수
    """

    if n <= 0:
        return
    if start < 2:
        start = 2

    # 이미 찾은 소수 개수
    count = 0

    # 현재 세그먼트 시작과 끝
    low = start
    high = low + segment_size

    while count < n:
        # isqrt(high) 이하의 소수 구하기
        limit = int(math.isqrt(high)) + 1
        base_sieve = bytearray(b'\x01') * (limit + 1)
        base_sieve[0:2] = b'\x00\x00'

        for i in range(2, limit + 1):
            if base_sieve[i]:
                base_sieve[i*i : limit + 1 : i] = b'\x00' * ((limit - i*i)//i + 1)

        base_primes = [i for i, is_prime in enumerate(base_sieve) if is_prime]

        # 세그먼트 생성
        sieve = bytearray(b'\x01') * (high - low)

        for p in base_primes:
            start = max(p*p, ((low + p - 1)//p) * p)
            if start >= high:
                continue
            sieve[start - low : high - low : p] = b'\x00' * ((high - start - 1)//p + 1)

        # 소수 yield
        for i, is_prime in enumerate(sieve):
            if is_prime:
                yield low + i
                count += 1
                if count >= n:
                    return

        # 세그먼트 확장
        low = high
        high = low + segment_size