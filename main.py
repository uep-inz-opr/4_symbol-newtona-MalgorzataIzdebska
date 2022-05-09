from math import *
#factorial(6)/(factorial(4)*factorial(2))

#from sys import stdin
#from math import factorial

def silnia(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

n, k = input("Enter two values: ").split()
n = int(n)
k = int(k)
 
if k == 0 or k == n:
	print ("1")
else : 
	print(silnia(n,k))

	