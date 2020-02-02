#!/usr/bin/python3
#Caesar cipher example
#Mostafa Dahshan <https://github.com/mdahshan>

P = 'abcdefghijklmnopqrstuvwxyz'
L = len(P)

def caesar(p, k):
	c = ''
	for pi in p:
		c += P[ (P.find(pi) + k) % L ]

	return c.upper()

#Example
if __name__ == "__main__":
	x = 'meetmeafterthetogaparty'
	y = caesar(x,3)
	print(y)
