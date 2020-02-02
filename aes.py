#!/usr/bin/python3
#AES cipher example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3


from Crypto.Cipher import AES

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
cipher = AES.new(key,AES.MODE_ECB)
x = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
y = cipher.encrypt(x)
z = cipher.decrypt(y)
print (z.hex())
