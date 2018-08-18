import random

def encrypt(data, key):
    dataPrep = []
    for i in data:
        dataPrep.append(ord(i))

    enc = []
    for i in range(len(dataPrep)):
        enc.append(chr(dataPrep[i] ^ key[i]))

    return ''.join(enc)
    
def generateKey(data):
    keyPrompt = input("Generate new key?(y/n):\n")
    key = []
    if keyPrompt == 'y':
        for i in range(len(data)):
            key.append(random.randint(1, 126))
        keyStr = ''.join(map(chr, key))
        k = open('key.txt', 'w')
        k.write(keyStr)
        k.close()
    elif keyPrompt == 'n':
        keyFile = input("Enter the filename of the key file (include '.txt')\n")
        k = open(keyFile, 'r')
        key = k.read()
        k.close()
        key = list(key)
        key = list(map(ord, key))
    return key

textFile = input("What file would you like to encrypt/decrypt (include '.txt')\n")
d = open(textFile, 'r')
data = d.read()
d.close()

key = generateKey(data)

dataPrompt = input("Are you encrypting or decrypting this file? ('e' for encrypt, 'd' for decrypt)\n")
if dataPrompt == 'e':
    enc = encrypt(data, key)
    encryptName = input("What filename would you like to store the encrypted data in? (include '.txt')\n")
    e = open(encryptName, 'w')
    e.write(str(enc))
    e.close()
elif dataPrompt == 'd':
    enc = encrypt(data, key)
    encryptName = input("What filename would you like to store the decrypted data in? (include '.txt')\n")
    e = open(encryptName, 'w')
    e.write(str(enc))
    e.close()
