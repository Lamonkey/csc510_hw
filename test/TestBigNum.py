import sys

sys.path.append('code')

from Num import *

def bignum():
	num = Num(None, None)
	num.capacity = 32
	for i in range(1,1000):
		num.add(i)
	# print(num.nums())
	return 32 == len(num.data)

tests = [bignum]