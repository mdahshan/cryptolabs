#!/usr/bin/python3
#RSA decryption example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
#https://www.tutorialspoint.com/python/python_files_io.htm
#https://courses.cs.washington.edu/courses/cse461/14wi/projects/proj4/natfiles/rsa_test.py

from Crypto.PublicKey import RSA

fb = open('key-b-private.pem','rb')
kb = RSA.importKey(fb.read())
fb.close()

f = open('c.bin','rb'); c = f.read(); f.close()

m = kb.decrypt(c).decode('utf-8')
print(m)
