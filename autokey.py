alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(plain,key):
    cipher = ""
    for index, i in enumerate(plain):
        if index is 0:
            cipher += alpha[(alpha.find(plain[0]) + key)]
        else:
            c = (alpha.find(i) + alpha.find(plain[index - 1])) % 26
            cipher += alpha[c]
    return(cipher)


def decrypt(cipher,key):
    plain = ""
    for index, i in enumerate(cipher):
        if index is 0:
            plain += alpha[(alpha.find(cipher[0]) - key)].lower()
        else:
            o = alpha.find(i) - alpha.find(plain[index - 1].upper())
            if(o < 0):
                o += 26
            plain += alpha[o].lower()
    return(plain)


def choice():
    print("(Autokey Algo)\n1.Encryption\n2.Decryption\n3.Exit"+"\n\n")
    ch = int(input("Enter choice:"))
    print("\n\n")
    if ch is 1:
        plain = str(input("Enter text to encrypt:").upper().replace(" ", ""))
        key = int(input("Enter key value"))
        print("Cipher text:" + encrypt(plain,key)+"\n\n")
    elif ch is 2:
        cipher = str(input("Enter text to decrypt:").upper().replace(" ", ""))
        key = int(input("Enter key value"))
        print("Plain text:" + decrypt(cipher,key)+"\n\n")
    elif ch is 3:
        pass
    else:
        print("Invalid choice"+"\n\n")


if __name__ == "__main__":
    plain = str(input("Enter text to encrypt:").upper().replace(" ", ""))
    key = int(input("Enter key value:"))
    print("Encrypted text : " + encrypt(plain,key))
    cipher = str(input("Enter text to decrypt:").upper().replace(" ", ""))
    key = int(input("Enter key value:"))
    print("Decrypted text : " + decrypt(cipher,key))
