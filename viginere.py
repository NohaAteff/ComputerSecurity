# Python code to implement
# Vigenere Cipher

# This function generates the 
# key in a cyclic manner until 
# it's length isn't equal to 
# the length of original text
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
# This function returns the 
# encrypted text generated 
# with the help of the key
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
# This function decrypts the 
# encrypted text and returns 
# the original text
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	

def vigenere_encrypt(plain, keyword):
	key = generateKey(plain.upper(), keyword.upper())
	cipher_text = cipherText(plain.upper(), key)
	print(f'plain text: {plain}')
	print(f'keyword: {keyword}')
	print(f'cipher text: {cipher_text}')

def vigenere_encrypt(plain, keyword):
    key = generateKey(plain.upper(), keyword.upper())
    cipher_text = cipherText(plain.upper(),key)
    print(f'plain text: {plain}')
    print(f'keyword: {keyword}')
    print(f'cipher text: {cipher_text}')
    return cipher_text.upper()
    
    
	
def vigenere_decrypt(cipher, keyword):
    key = generateKey(cipher.upper(), keyword.upper())
    plain_text = originalText(cipher.upper(), key)
    return plain_text.lower()
# vigenere_encrypt('ahmed', 'play')
# vigenere_decrypt('psmcs', 'play')