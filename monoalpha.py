#!/usr/bin/python3
#Mono alphabetic cipher example
#Mostafa Dahshan <https://github.com/mdahshan>

P = 'abcdefghijklmnopqrstuvwxyz'

def monoalpha(p, k):
	c = ''
	for pi in p:
		c += k[P.find(pi)]

	return c.upper()

#Example
if __name__ == "__main__":
	x = 'ifwewishtoreplaceletters'
	k = 'dkvqfibjwpescxhtmyauolrgzn'
	y = monoalpha(x,k)
	print(y)
