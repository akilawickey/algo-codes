import string

def shifttext(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    print(alphabet[shift:])
    print(alphabet[:shift] )
    table = string.maketrans(alphabet,shifted_alphabet)
    print(plaintext.translate(table))
    return plaintext.translate(table)


a = raw_input().strip()
b = shifttext(a, 15)
# print(b)
