def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) - len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
def encrypt(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) + ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
def decrypt(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	
if __name__ == "__main__":
	string = "HELLO"
	keyword = "WORLD"
	key = generateKey(string, keyword)
	cipher_text = encrypt(string,key)
	print("Ciphertext :", cipher_text)
	print("Decrypted Text :", decrypt(cipher_text, key))
