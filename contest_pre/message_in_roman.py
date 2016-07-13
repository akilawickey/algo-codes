import string

s = []
def shifttext(plaintext, shift):
    alphabet = string.ascii_lowercase
    table = " "
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(shifted_alphabet,alphabet)


    return plaintext.translate(table)
def shifttext_a(plaintext, shift):
    alphabet = string.ascii_lowercase
    table = " "
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet,shifted_alphabet)


    return plaintext.translate(table)

for i in range(int(raw_input())):

    a = raw_input().strip()
    shift = (ord("u") - ord(a[-1]))
    a = a[:-1]
    #print(shift)

    if shift < 0:
        shift = abs(shift)
        b = shifttext(a, shift)
        print(b)
    else:

        b = shifttext_a(a, shift)
        print(b)




