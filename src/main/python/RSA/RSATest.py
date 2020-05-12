from RSA import RSAImpl as rsa

print('Test 1:')
n, e, d = rsa.rsa_algorithm(p=11, q=3, e=3)
print('Public Key: ', (n, e), '\nPrivate Key: ', (n, d))
# Public key = (n, e) = (33, 3)
# Private key = (n, d) = (33, 7)

print('Test 2:')
n, e, d = rsa.rsa_algorithm(p=173, q=149, e=3)
print('Public Key: ', (n, e), '\nPrivate Key: ', (n, d))
# Public key = (n, e) = (25777, 3)
# Private key = (n, d) = (25777, 16971)


# test for random numbers
for i in range(3, 11):
    print('Test ', i, ':')
    n, e, d = rsa.rsa_algorithm()
    print('Public Key: ', (n, e), '\nPrivate Key: ', (n, d))
