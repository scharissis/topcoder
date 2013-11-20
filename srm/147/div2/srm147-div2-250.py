""" 
	TopCoder - SRM 147, DIV 2, 250
"""

import array,bisect,collections,fractions,heapq,itertools,math,re,string 

class CCipher:
	def decode(self, cipherText, shift):
		table = {}
		z, a = ord('Z'), ord('A')
		for l in range(z-a+1):
			table[chr(a+l)] = chr(a+(l-shift)%(z-a+1))
		plain = ""
		for l in cipherText:
			plain += table[l]
		return plain


tests = {
	"TOPCODER": ["VQREQFGT",2],
}
c = CCipher()
for t in tests:
	res = c.decode(*tests[t])
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL', res
