#!/usr/bin/python3
#Vigenere cipher example
#Mostafa Dahshan <https://github.com/mdahshan>

P = 'abcdefghijklmnopqrstuvwxyz'
L = len(P)

def vigenere(p, k):
	c = ''
	i = 0
	l = len(k)

	for pi in p:
		c += P[ (P.find(pi) + P.find(k[i%l])) % L]
		i += 1

	return c.upper()

#Example
if __name__ == "__main__":
	x = 'wearediscoveredsaveyourself'
	k = 'deceptive'
	y = vigenere(x,k)
	print(y)
