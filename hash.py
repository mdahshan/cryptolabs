#!/usr/bin/python3
#Hash example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.Hash.SHA256.SHA256Hash-class.html

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
cipher = AES.new(key,AES.MODE_ECB)
m = 'Check signatures'.encode('utf-8')
mlen = len(m).to_bytes(1,'little')
hash = SHA256.new()
hash.update(m)
h = hash.hexdigest()
sm = m+cipher.encrypt(h)
f = open('h.bin','wb')
f.write(mlen+sm)
f.close()
