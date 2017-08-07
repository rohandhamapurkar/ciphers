from random import randint as ri

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plaintext):
    ciphertext = ""
    for index, i in enumerate(plaintext):
        key = ri(0, 25)
        char = alpha.find(i) + key
        if char >= 26:
            char = char % 26
        ciphertext += alpha[char] 
    return ciphertext

def choice():
    print("(OneTimePad Cipher)\n1.Encryption\n2.Exit"+"\n\n")
    ch = int(input("Enter choice:"))
    print("\n\n")
    if ch is 1:
        plain = str(input("Enter text to encrypt: ").replace(" ","").upper())
        print("Cipher text:"+encrypt(plain)+"\n\n")
    elif ch is 2:
        pass
    else:
        print("Invalid choice"+"\n\n")
