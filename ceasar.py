alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plain):
    cipher = ""
    for index, i in enumerate(plain):
        c = alpha.find(i.upper()) + 3
        if(c >= 26):
            c = c % 26
        cipher += alpha[c]
    return(cipher)


def decrypt(cipher):
    plain = ""
    for index, i in enumerate(cipher):
        c = alpha.find(i) - 3
        if(c < 0):
            c += 26
        plain += alpha[c].lower()
    return(plain)


def choice():
    print("(Ceasar Cipher)\n1.Encryption\n2.Decryption\n3.Exit"+"\n\n")
    ch = int(input("Enter choice:"))
    print("\n\n")
    if ch is 1:
        plain = str(input("Enter text to encrypt: ").replace(" ", "").upper())
        print("Cipher text:" + encrypt(plain)+"\n\n")
    elif ch is 2:
        cipher = str(input("Enter text to decrypt: ").replace(" ", "").upper())
        print("Plain text:"+decrypt(cipher)+"\n\n")
    elif ch is 3:
        pass
    else:
        print("Invalid choice"+"\n\n")

if __name__ == "__main__":
    plain = str(input("Enter text to encrypt: ").replace(" ",""))
    print("Encrypted text : "+encrypt(plain.upper()))
    cipher = str(input("Enter text to decrypt: ").replace(" ",""))
    print("Decrypted text : "+decrypt(cipher.upper()))
