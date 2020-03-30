L = [1, 3, 5, 6, 8, 10, 12, 14, 13, 99]

def binarySearch(x, y, L):
	sup = y
	inf = 0
	searchBin = 0
	notFound = -1
	while inf <= sup:
		try:
			meio = int((sup+inf)/2)
			if L[meio] == x:
				searchBin = meio
				notFound = 1
				return searchBin
			elif L[meio] < x:
				inf += 1
			else:
				sup -= 1
		except IndexError:
			break
	if notFound == -1:
		return searchBin

#============================================#

element = int(input())
A = binarySearch(element, len(L), L)
print(A)

