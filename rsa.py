def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
import math
def rsa_encrypt(p, q, m):
    e = 0
    d = 0
    if(is_prime(p) and is_prime(q)):
        n = p * q
        phi_n = (p - 1) * (q - 1)
        for i in range(1, phi_n + 1):
            if(is_prime(i) and phi_n % i != 0):
                e = i
                break
        while((e * d) % 20 != 1):
            d += 1
        c = math.pow(m, e) % n
    return c

def rsa_decrypt(p, q, c):
    e = 0
    d = 0
    if(is_prime(p) and is_prime(q)):
        n = p * q
        phi_n = (p - 1) * (q - 1)
        for i in range(1, phi_n + 1):
            if(is_prime(i) and phi_n % i != 0):
                e = i
                break
        while((e * d) % 20 != 1):
            d += 1
        m = math.pow(c, d) % n
    return m