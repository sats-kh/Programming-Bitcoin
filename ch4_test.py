from ecc import S256Point, Signature, PrivateKey
# Quiz 4.1
p = PrivateKey(5000).point
print(p.sec().hex())

p = PrivateKey(2018**5).point
print(p.sec().hex())

p = PrivateKey(0xdeadbeef12345).point
print(p.sec().hex())

# Quiz 4.2
p = PrivateKey(5001).point
print(p.sec(compressed=True).hex())
p = PrivateKey(2019**5).point
print(p.sec(compressed=True))
p = PrivateKey(0xdeadbeef54321).point
print(p.sec(compressed=True))

# Quiz 4.3
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6

s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

sig = Signature(r, s)
print(sig.der().hex())

# example 4.4: Base58
from helper import encode_base58
h = '7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'
print(encode_base58(bytes.fromhex(h)))

h = 'eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c'
print(encode_base58(bytes.fromhex(h)))

h = 'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6'
print(encode_base58(bytes.fromhex(h)))

# Quiz 4.5
p = PrivateKey(5000).point
print(p.address(compressed=False, testnet=True))
p = PrivateKey(2020**5).point
print(p.address(testnet=True))
p = PrivateKey(0x12345deadbeef).point
print(p.address())

# Quiz 4.6
p = PrivateKey(5003)
print(p.wif(compressed=True, testnet=True))

p = PrivateKey(2021**5)
print(p.wif(compressed=False, testnet=True))

p = PrivateKey(0x54321deadbeef)
print(p.wif(compressed=True, testnet=False))

# Quiz 4.7
def little_endian_to_int(b):
    '''little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer'''
    return int.from_bytes(b, 'little')

# Quiz 4.8
def int_to_little_endian(n, length):
    '''int_to_little_endian takes an integer and returns the little-endian byte sequence of length'''
    return n.to_bytes(length, 'little')

# Quiz 4.9
from helper import hash256
passphrase = b'kwanhoon@snu.ac.kr-my_secret'
secret = little_endian_to_int(hash256(passphrase))
p = PrivateKey(secret)
p.point.address(testnet=True)
