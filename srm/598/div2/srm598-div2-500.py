"""
	TopCoder - SRM 598, DIV 2, 500

	Passes all system tests.
"""
import copy

class BinPackingEasy:
	def minBins(self, item):
		num_b = 0
		item = sorted(item)
		while len(item) > 0:
			b = [item.pop()]
			idx = []
			i2 = copy.copy(item)
			for x in xrange(0,len(i2)):
				if i2[::-1][x] + sum(b) <= 300:
					b += [i2[::-1][x]]
					idx += [x]
			for d in idx:
				del item[len(item)-1-d]
			if len(b) > 0 : 
				num_b += 1
		return num_b


tests = {
	3: [150,150,150,150,150],
	2: [130,140,150,160],
	6: [101,200,101,101,101,101,200,101,200],
}
c = BinPackingEasy()
for t in tests:
	ans = t
	q = tuple(tests[t])
	res = c.minBins(q)
	if res != ans:
		print 'FAIL', res
	else:
		print 'PASS'	
