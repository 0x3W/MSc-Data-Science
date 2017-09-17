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
	
