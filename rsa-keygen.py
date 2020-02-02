#!/usr/bin/python3
#RSA key generation example
#Mostafa Dahshan <https://github.com/mdahshan>

#References
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html
#https://www.tutorialspoint.com/python/python_files_io.htm
#https://courses.cs.washington.edu/courses/cse461/14wi/projects/proj4/natfiles/rsa_test.py

from Crypto.PublicKey import RSA

key = RSA.generate(1024)
print('Public key information:')
print('Modulus (n):',key.n)
print('Exponent (e):',key.e)
print('Private (d):',key.d)

if input('Save to file (y/N)? ').lower() == 'y':
	f = open('key-private.pem','wb')
	f.write(key.exportKey('PEM'))
	f.close()
	
	f = open('key-public.pem','wb')
	f.write(key.publickey().exportKey('PEM'))
	f.close()
