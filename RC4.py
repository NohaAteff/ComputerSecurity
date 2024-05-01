import base64

def ksa(key):
    """Key-scheduling algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, length):
    """Pseudo-random generation algorithm (PRGA)"""
    i = 0
    j = 0
    key_stream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_stream.append(S[(S[i] + S[j]) % 256])
    return key_stream

def text_to_binary(text):
    """Convert text to binary string"""
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string

def binary_to_text(binary_string):
    """Convert binary string to text"""
    text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    return text

def rc4_encrypt(data, key):
    """Encrypt data using RC4 algorithm"""
    S = ksa(key)
    key_stream = prga(S, len(data))
    encrypted = bytes([data[i] ^ key_stream[i] for i in range(len(data))])
    return encrypted

def rc4_decrypt(data, key):
    """Decrypt data using RC4 algorithm"""
    return rc4_encrypt(data, key)  # RC4 decryption is the same as encryption
# print(rc4_encrypt('0100100001001001','01000101'))