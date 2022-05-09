from math import *
#factorial(6)/(factorial(4)*factorial(2))

#from sys import stdin
#from math import factorial

def silnia(n, k):
	return factorial(n) // (factorial(k) * factorial(n-k))

t = input()
n, k = input().split()
 
for i in range(t):
	n,k = map(int, input().split())
	if k == 0 or k == n : print ("1")
	else : print (silnia(n, k))

	n = int(6)
	k = int(4)
	print (silnia(n, k))

	