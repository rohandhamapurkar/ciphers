alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain):
	cipher = ""
	for index,i in enumerate(plain):
		c = alpha.find(i.upper())+3
		if(c>26):
			c = c%26
		cipher += alpha[c]
	return(cipher)

def decrypt(cipher):
	plain = ""
	for index,i in enumerate(cipher):
		c = alpha.find(i)-3
		if(c<0):
			c+=26
		plain += alpha[c].lower()
	return(plain)

if __name__ == "__main__":
	plain = str(input("Enter text to encrypt: ").replace(" ",""))
	print("Encrypted text : "+encrypt(plain.upper()))
	cipher = str(input("Enter text to decrypt: ").replace(" ",""))
	print("Decrypted text : "+decrypt(cipher.upper()))