#!/usr/bin/python3
#Hash example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.Hash.HMAC-module.html

from Crypto.Hash import HMAC

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
m = 'Message must be authenticated'.encode('utf-8')
mlen = len(m).to_bytes(1,'little')
mac = HMAC.new(key)
mac.update(m)
sm = m+mac.digest()
f = open('hmac.bin','wb')
f.write(mlen+sm)
f.close()

