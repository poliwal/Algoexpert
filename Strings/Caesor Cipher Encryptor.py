# O(n) time | o(n) space
def caesorCipherEncryptor(string, key):
	key = key % 26
	encryptedString = []
	for char in string:
		encryptedString.append(getEncryptedChar(char, key))
	return "".join(encryptedString)

def getEncryptedChar(char, key):
	charCode = ord(char) + key
	return chr(charCode) if charCode <= 122 else chr(96 + charCode % 122)


print(caesorCipherEncryptor('xyz', 2))