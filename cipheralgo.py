from autokey import choice as a
from ceasar import choice as c
from onetimepad import choice as o
from additive import choice as ad


def main():
    while True:
        print("Cryptographic Algorithms\n1.Autokey Cipher\n2.Ceasar Cipher\n3.OneTimePad Cipher\n4.Additive Cipher\n5.Exit"+"\n\n")
        ch = int(input("Enter choice:"))
        print("\n\n")
        if ch is 1:
            a()
        elif ch is 2:
            c()
        elif ch is 3:
            o()
        elif ch is 4:
            ad()
        elif ch is 5:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
