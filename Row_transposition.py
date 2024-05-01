def row_transposition_encrypt(plain_text, key):
    key = str(key)
    print(key, len(key))
    """Encrypt text using Raw Transposition algorithm"""
    # Initialize a dictionary to store characters for each column
    columns = {i: [] for i in range(1, len(key) + 1)}

    # Fill the columns with characters from the plain text
    index = 0
    key = int(key)
    for char in plain_text:
        columns[(index % key) + 1].append(char)
        index += 1

    # Concatenate characters from each column to form the cipher text
    cipher_text = ''
    for col in range(1, key + 1):
        cipher_text += ''.join(columns[col])

    return cipher_text

def row_transposition_decrypt(cipher_text, key):
    """Decrypt text using Raw Transposition algorithm"""
    # Calculate the number of rows required based on the key
    rows = len(cipher_text) // key
    if len(cipher_text) % key != 0:
        rows += 1

    # Initialize a list of empty strings to represent the rows
    rows_list = [''] * rows

    # Fill the rows with characters from the cipher text
    for i in range(len(cipher_text)):
        rows_list[i % rows] += cipher_text[i]

    # Concatenate characters from each row to form the decrypted text
    decrypted_text = ''.join(rows_list)

    return decrypted_text

# print(row_transposition_encrypt('information security',345216))