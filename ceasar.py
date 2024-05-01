def caesar_cipher(text, shift = 3):
    text = text.upper()
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            # Leave non-alphabetic characters unchanged
            result += ''
    return result.upper()

def caesar_decipher(text, shift = 3):
    text = text.upper()
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            # Leave non-alphabetic characters unchanged
            result += ''
    return result.lower()

# print(caesar_decipher('gcuavqdtgcm',2))