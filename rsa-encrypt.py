#!/usr/bin/python3
#RSA encryption example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
#https://www.tutorialspoint.com/python/python_files_io.htm
#https://courses.cs.washington.edu/courses/cse461/14wi/projects/proj4/natfiles/rsa_test.py

from Crypto.PublicKey import RSA

fb = open('key-b-public.pem','rb')
kb = RSA.importKey(fb.read())
fb.close()

m = 'Only B can decrypt this'
c = kb.encrypt(m.encode('utf-8'),0)[0]

f = open('c.bin','wb'); f.write(c); f.close()
print(c)
