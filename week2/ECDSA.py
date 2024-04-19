from ecpy.curves import Curve
from sha3 import keccak_256
import random

private_key = 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
cv = Curve.get_curve('secp256k1')
G = cv.generator

def generate_public_key(private_key):
    public_key = private_key * G 

    return public_key


def hash_message(message):
    h = '0x' + keccak_256(message.encode()).digest().hex() 

    return h

def ECDSA_sign(message, private_key):
    public_key = generate_public_key(private_key)
    h = hash_message(message)
    
    k = random.randrange(1, n) # generate a random number between 1 to n
    R = k * G
    r = R.x % n # r is the x coordinate of R
    s = pow(k, -1, n) * (int(h, 16) + r * private_key) % n # signature proof
    
    return r, s, h, public_key

def ECDSA_verify_signature(r, s, h, public_key):
    s1 = pow(s, -1, n)
    R_prime = (int(h, 16) * s1)* G + (r * s1 ) * public_key
    r_prime = R_prime.x % n # r' is the x coordinate of R'

    return r_prime == r


def main(message):
    r, s, h, public_key = ECDSA_sign(message, private_key)
    result = ECDSA_verify_signature(r, s, h, public_key)
    
    if result:
        print("signature verified!")
    else:
        print("signature is invalid.")

