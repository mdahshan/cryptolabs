#!/usr/bin/python3
#ECB Cipher mode example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
#https://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes
#https://www.tutorialspoint.com/python/python_files_io.htm

from Crypto.Cipher import AES

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')

#ECB mode
ecb = AES.new(key,AES.MODE_ECB)
fi  = open('plain.bmp', 'rb')
hdr = fi.read(108) #read bmp header
x   = fi.read() #read to the end
fi.close()
pad = bytes(16 - len(x)%16) #pad to block
y   = ecb.encrypt(x+pad)
fo  = open('cipher-ecb.bmp', 'wb')
fo.write(hdr+y)
fo.close()
