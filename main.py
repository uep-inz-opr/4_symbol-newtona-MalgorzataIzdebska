from sys import stdin
from math import factorial

def silnia(n, k):
	return factorial(n) // (factorial(k) * factorial(n-k))
wynik=int(stdin.readline());
if(wynik)
	n,k=input().split()
	n=int(6)
	k=int(4)
	print(silnia(n.k))
	wynik=wynik-1