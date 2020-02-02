#!/usr/bin/python3
#Hash verify example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.Hash.SHA256.SHA256Hash-class.html
#https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
#https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3


from Crypto.Cipher import AES
from Crypto.Hash import SHA256

f = open('h.bin','rb')
mlen = int.from_bytes(f.read(1),'little')
m = f.read(mlen)
hsc = f.read()

key = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
cipher = AES.new(key,AES.MODE_ECB)
hs = cipher.decrypt(hsc).decode('utf-8')

hash = SHA256.new()
hash.update(m)
h = hash.hexdigest()

print('Message [{}]. Hash valid [{}]'.format(m.decode('utf-8'), h==hs))
