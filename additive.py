alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plain, key):
    cipher = ""
    for index, i in enumerate(plain):
        c = alpha.find(i.upper()) + key
        if(c >= 26):
            c = c % 26
        cipher += alpha[c]
    return(cipher)


def decrypt(cipher, key):
    plain = ""
    for index, i in enumerate(cipher):
        c = alpha.find(i) - key
        if(c < 0):
            c += 26
        plain += alpha[c].lower()
    return(plain)


def choice():
    print("(Additive Cipher)\n1.Encryption\n2.Decryption\n3.Exit"+"\n\n")
    ch = int(input("Enter choice:"))
    print("\n\n")
    if ch is 1:
        plain = str(input("Enter text to encrypt: ").replace(" ", "").upper())
        key = int(input("Enter key value:"))
        print("Cipher text:" + encrypt(plain, key)+"\n\n")
    elif ch is 2:
        cipher = str(input("Enter text to decrypt: ").replace(" ", "").upper())
        key = int(input("Enter key value:"))
        print("Plain text:" + decrypt(cipher, key)+"\n\n")
    elif ch is 3:
        pass
    else:
        print("Invalid choice"+"\n\n")


if __name__ == "__main__":
    plain = str(input("Enter text to encrypt: ").replace(" ", ""))
    key = input("Enter key value:")
    print("Encrypted text : "+encrypt(plain.upper(),key))
    cipher = str(input("Enter text to decrypt: ").replace(" ",""))
    key = input("Enter key value:")
    print("Decrypted text : "+decrypt(cipher.upper(),key))
