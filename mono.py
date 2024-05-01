def monoalphabetic_encrypt(plaintext,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key
    print(key,plaintext)
    msg = plaintext
    msg = [i for i in msg]
    pt = [i for i in alphabet]
    k = [i for i in key]

    print(len(pt))

    print(len(k))
    mono = {pt[i]: k[i] for i in range(len(pt))}
    print(mono)
    encr = ''
    for i in msg:
        if i==' ':
            continue
        else:
            encr+=mono[i]
    cipher = "".join(map(str,encr))
    # print("".join(map(str,en)))
    return cipher

def monoalphabetic_decrypt(cipher,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key

    msg = cipher
    msg = [i for i in msg]
    pt = [i for i in alphabet]
    k = [i for i in key]
    mono = {pt[i]: k[i] for i in range(len(pt))}

    plaintext = ''
    for char in cipher:
    # Find the corresponding key (original letter) from the mono dictionary
        for key, value in mono.items():
            if value == char:
                plaintext += key
                break
    return plaintext

# print(monoalphabetic_encrypt('monoalphabetic','mnbvcxzasdfghjklpoiuytrewq'))
# print(monoalphabetic_decrypt('hkjkmglamncusb','mnbvcxzasdfghjklpoiuytrewq'))

