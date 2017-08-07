import random
import math
smallPrimes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
e = 0
d = 0
n = 0


def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def is_large_prime(num):
    if (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(math.sqrt(num)) + 1, 2))


def get_prime():
    while True:
        a = random.getrandbits(20)
        if(is_large_prime(a)):
            return a
            break


def calculation():
    p = get_prime()
    q = get_prime()
    global n
    n = p * q
    phi = (p - 1) * (q - 1)

    global e
    e = random.choice(smallPrimes)

    k = 1
    global d
    while True:
        d = ((k * phi) + 1) / float(e)
        if (d % 1 == 0):
            break
        if(k > 1000):
            e = random.choice(smallPrimes)
        k += 1


def encrypt(pt):
    calculation()
    cipher = pow(int(pt), int(e), n)
    print("Original Plain Text:" + str(pt))
    print("Cipher Text:" + str(cipher))
    return cipher


def decrypt(ct, d, n):
    pt = pow(int(ct), int(d), n)
    print("Decrypted Text:" + str(pt))


if __name__ == "__main__":
    cipher = encrypt(100)
    decrypt(cipher, d, n)
