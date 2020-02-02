#!/usr/bin/python3
#Hash example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.Hash.HMAC-module.html

from Crypto.Hash import HMAC

f = open('hmac.bin','rb')
mlen = int.from_bytes(f.read(1),'little')
m = f.read(mlen)
msc = f.read()

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
mac = HMAC.new(key)
mac.update(m)

print('Message [{}]. MAC valid [{}]'.format(m.decode('utf-8'), mac.digest()==msc))

