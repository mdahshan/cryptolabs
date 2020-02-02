#!/usr/bin/python3
#CBC Cipher mode example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
#https://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes
#https://www.tutorialspoint.com/python/python_files_io.htm

from Crypto.Cipher import AES

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
iv  = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
#CBC mode
cbc = AES.new(key,AES.MODE_CBC,iv)
fi  = open('plain.bmp', 'rb')
hdr = fi.read(108) #read bmp header
x   = fi.read() #read to the end
fi.close()
pad = bytes(16 - len(x)%16) #pad to block
y   = cbc.encrypt(x+pad)
fo  = open('cipher-cbc.bmp', 'wb')
fo.write(hdr+y)
fo.close()
