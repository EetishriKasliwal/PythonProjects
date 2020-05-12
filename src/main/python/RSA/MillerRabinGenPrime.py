from random import randrange, getrandbits


def is_prime(num, no_of_tests=128):
    """ Test if a number is prime
        Args:
            num -- int -- the number to test
            no_of_tests -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if num is not even.
    if num <= 1 or num % 2 == 0:
        return False

    # find r and s
    s = 0
    r = num - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    # perform tests no_of_tests times
    for _ in range(no_of_tests):
        a = randrange(2, num - 1)
        x = pow(a, r, num)
        if x != 1 and x != num - 1:
            j = 1
            while j < s and x != num - 1:
                x = pow(x, 2, num)
                if x == 1:
                    return False
                j += 1
            if x != num - 1:
                return False
    return True


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    genratedNum = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    genratedNum |= (1 << length - 1) | 1
    return genratedNum


def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    num = 10
    # keep generating while the primality test fail
    while not is_prime(num, 128):
        num = generate_prime_candidate(length)
    return num
