from RSA import MillerRabinGenPrime as mrg


def modInverse(e, phi):
    """ calculate mod inverse
        Args:
            e -- int -- chosen encryption exponent
            phi -- int -- (p-1)*(quotient-1)
        return True if n is prime
    """
    phi0, y_coeff, x_coeff = phi, 0, 1
    if phi == 1:
        return 0
    while e > 1:
        # quotient is quotient
        temp = phi
        quotient = e // phi
        # phi is remainder now, process
        phi = e % phi
        e = temp
        temp = y_coeff
        # Update x_coeff and y_coeff
        y_coeff = x_coeff - quotient * y_coeff
        x_coeff = temp
    # Make x_coeff positive
    if x_coeff < 0:
        x_coeff = x_coeff + phi0
    return x_coeff


def rsa_algorithm(p=None, q=None, e=65537, length=1024):
    """ calculate mod inverse
            Args:
                p -- int -- first prime
                q -- int -- second prime
                e -- int -- chosen encryption exponent
                length -- int -- bit size of n
                e -- int -- chosen encryption exponent
                phi -- int -- (p-1)*(quotient-1)
            return True if n is prime
        """

    # e = 2 ** 2 ** x + 1 but to avoid complexity we should chose e as 65537.
    if not p:
        while True:
            p = mrg.generate_prime_number(length // 2)
            if p % e != 1:
                break
    if not q:
        while True:
            q = mrg.generate_prime_number(length - length // 2)
            if q % e != 1 and q != p:
                break

    if p < q:
        p, q = q, p

    n = p * q
    phi = (p - 1) * (q - 1)
    d = modInverse(e, phi)

    return n, e, d
