from sys import stdin
from math import factorial

def silnia(n, k):
	return factorial(n) // (factorial(k) * factorial(n-k))

#t=int(stdin.readline());
t = int( raw_input() )
 
for i in range(t):
	n,k = map( int, raw_input().split() )
	if k == 0 or k == n : print '1'
	else : print silnia(n,k)

#while(t):
	#n,k=input().split()
	#n=int(6)
	#k=int(4)
	#print(silnia(n,k))
	