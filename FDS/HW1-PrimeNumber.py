# Identify a prime number

import sys
p = int(input('Tell me a number: '))

def prime(n):
	if n == 2 or n == 3:
		print("Prime") 
		sys.exit()
	elif n < 2:
		print("Choose bigger number, and run program again")
		sys.exit()
	elif n%2 == 0:
		print("2")
		sys.exit()	
	elif n < 9:
		print("Prime")
		sys.exit()
	elif n%3 == 0: 
		print("3")
		sys.exit()
	sqRt = int(n**0.5)
	i = 5
	while i <= sqRt:
		if n%i == 0: 
			print(i)
			sys.exit()
		elif n%(i+2) == 0:
			print(i+2)
			sys.exit()
		else:
			i +=6
	print("Prime")     
prime(p)
