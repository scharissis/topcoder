""" 
	TopCoder - SRM 148, DIV 2, 250

	Passes system tests.
"""

import array,bisect,collections,fractions,heapq,itertools,math,re,string 

class DivisorDigits:
	def howMany(self,N):
		original = N
		count = 0
		last = 0
		while N > 0:
			last = N%10
			if last!= 0 and original%last == 0:
				count += 1
			N = N/10
		return count

tests = {
	2: 12,
	3: 661232,
}
c = DivisorDigits()
for t in tests:
	p = tests[t]
	res = c.howMany(p)
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL', p, 'returned', res
