
# def caesar_cipher(text, shift):
#     text = text.upper()
#     result = ""
#     for char in text:
#         if char.isalpha():
#             result += chr((ord(char) + shift - 65) % 26 + 65)
#         else:
#             # Leave non-alphabetic characters unchanged
#             result += ''
#     return result.upper()

# # ci = caesar_cipher('hello world',3)
# # print(ci)
def DES(plaintext,key,p10,p8,IP,EP,p4,IP_inv):
    pass
def string_to_list(a):
    result = []
    temp = ""
    for char in a:
        if char.isdigit():
            temp += char
            if len(temp) > 1 and temp[0] == '1' and int(temp) > 10:
                result.append(int(temp[:-1]))
                temp = temp[-1]
            elif int(temp) > 10:
                result.append(int(temp[:-1]))
                temp = temp[-1]
        else:
            raise ValueError("Invalid character in input string")
    if temp:
        result.append(int(temp))
    return result
def bin_to_list(a):
    a = [int(i) for i in a]
    return a
print(string_to_list('547101'))
print(bin_to_list('10010'))
# int key[]= {0,0,1,0,0,1,0,1,1,1};
key = bin_to_list('1010000010')  # extra example for checking purpose
P10 = string_to_list('35274101986')
P8 = string_to_list("637485109")

IP = string_to_list('26314857')
EP = string_to_list("41232341")
P4 = string_to_list("2431")
IP_inv = string_to_list("41357286")

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def key_generation():
    key_ = [key[P10[i] - 1] for i in range(10)]

    Ls = key_[:5]
    Rs = key_[5:]

    Ls_1 = shift(Ls, 1)
    Rs_1 = shift(Rs, 1)

    key_[:5] = Ls_1
    key_[5:] = Rs_1

    key1 = [key_[P8[i] - 1] for i in range(8)]

    Ls_2 = shift(Ls, 2)
    Rs_2 = shift(Rs, 2)

    key_[:5] = Ls_2
    key_[5:] = Rs_2

    key2 = [key_[P8[i] - 1] for i in range(8)]

    print("Your Key-1 :")
    print(" ".join(map(str, key1)))
    print("Your Key-2 :")
    print(" ".join(map(str, key2)))
    return key1,key2

def shift(ar, n):
    while n > 0:
        temp = ar[0]
        ar = ar[1:] + [temp]
        n -= 1
    return ar

def encryption(plaintext):
    plaintext = bin_to_list(plaintext)
    key1,key2 = key_generation()
    arr = [plaintext[IP[i] - 1] for i in range(8)]
    arr1 = function_(arr, key1)
    after_swap = swap(arr1, len(arr1) // 2)
    arr2 = function_(after_swap, key2)
    ciphertext = [arr2[IP_inv[i] - 1] for i in range(8)]
    return (" ".join(map(str, ciphertext))),ciphertext,key1,key2

def binary_(val):
    return bin(val)[2:].zfill(2)

def function_(ar, key_):
    l = ar[:4]
    r = ar[4:]

    ep = [r[EP[i] - 1] for i in range(8)]

    ar = [key_[i] ^ ep[i] for i in range(8)]

    l_1 = ar[:4]
    r_1 = ar[4:]

    row = int("".join(map(str, [l_1[0], l_1[3]])), 2)
    col = int("".join(map(str, [l_1[1], l_1[2]])), 2)
    val = S0[row][col]
    str_l = binary_(val)

    row = int("".join(map(str, [r_1[0], r_1[3]])), 2)
    col = int("".join(map(str, [r_1[1], r_1[2]])), 2)
    val = S1[row][col]
    str_r = binary_(val)

    r_ = [int(str_l[i]) for i in range(2)] + [int(str_r[i]) for i in range(2)]
    r_p4 = [r_[P4[i] - 1] for i in range(4)]

    l = [l[i] ^ r_p4[i] for i in range(4)]

    output = l + r
    return output

def swap(array, n):
    l = array[:n]
    r = array[n:]
    output = r + l
    return output

def decryption(ar):
    key1,key2=key_generation()
    arr = [ar[IP[i] - 1] for i in range(8)]
    arr1 = function_(arr, key2)
    after_swap = swap(arr1, len(arr1) // 2)
    arr2 = function_(after_swap, key1)
    decrypted = [arr2[IP_inv[i] - 1] for i in range(8)]
    return (" ".join(map(str, decrypted)))

# key_generation()

# int []plaintext= {1,0,1,0,0,1,0,1};
plaintext = [0,1,0,1,1,1,1,0]  # extra example for checking purpose
# plaintext = bin_to_list("01011110")
# print("\nYour plain Text is :")
# print(" ".join(map(str, plaintext)))

ciphertext,CipherText,_,_ = encryption(plaintext)

print("\nYour cipher Text is : ",ciphertext)
# print(" ".join(map(str, ciphertext)))

# decrypted = decryption(CipherText)

# print("\nYour decrypted Text is : ",decrypted)
# print(" ".join(map(str, decrypted)))




