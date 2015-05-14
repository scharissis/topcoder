"""
	TopCoder - SRM 652, DIV 2, Level 1
"""

from collections import defaultdict

class ValueOfString:
	val = {}
	for i in xrange(0,26):
		l = str(unichr(ord('a')+i))
		val[l] = i+1

	def findValue(self, s):
		numLower, total = defaultdict(int), 0
		for l in set(s):
			for m in s:
				if self.val[m] <= self.val[l]:
					numLower[l] += 1
					
		for l in s:
			total += self.val[l] * numLower[l]
		return total

tests = {
	"babca": 35,
	"zz": 104,
	"y": 25,
	"aaabbc": 47,
	"topcoder": 558,
	"thequickbrownfoxjumpsoverthelazydog": 11187,
	"zyxwvutsrqponmlkjihgfedcba": 6201
}
c = ValueOfString()
for i,expected in tests.iteritems():
	res = c.findValue(i)
	if res != expected:
		print "FAIL: Got {0}, Expected {1}".format(res, expected)
	else:
		print 'PASS'
