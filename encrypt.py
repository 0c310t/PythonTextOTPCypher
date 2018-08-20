import random

def encrypt(data, key):
    dataPrep = []
    for i in data:
        dataPrep.append(i)

    enc = []
    for i in range(len(dataPrep)):
        enc.append(dataPrep[i] ^ key[i % 1023])

    return bytes(enc)
    
def generateKey(data):
    keyPrompt = input("Generate new key?(y/n):\n")
    key = []

    while keyPrompt not in ('y', 'n'):
        print('Invalid input.')
        keyPrompt = input("Generate new key?(y/n):\n")
    
    if keyPrompt == 'y':
        for i in range(1024):
            key.append(random.randint(1, 255))
        keyStr = bytes(key)
        k = open('key.txt', 'wb')
        k.write(keyStr)
        k.close()
    elif keyPrompt == 'n':
        while True:
            try:
                keyFile = input("Enter the filename of the key file (include file type)\n")
                k = open(keyFile, 'rb')
                key = k.read()
                k.close()
            except FileNotFoundError:
                print("That file does not exist.")
                pass
            else:
                break
        
    return key

while True:
    try:
        textFile = input("What file would you like to encrypt/decrypt (include file type)\n")
        d = open(textFile, 'rb')
        data = d.read()
        d.close()
    except FileNotFoundError:
        print("That file does not exist.")
        pass
    else:
        break
    
key = generateKey(data)

enc = encrypt(data, key)
encryptName = input("What filename would you like to store the encrypted/decrypted data in? (include file type')\n")
encryptList = encryptName.split('.')
e = open(encryptName, 'wb')
e.write(enc)
e.close()
