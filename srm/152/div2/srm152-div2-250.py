"""
	TopCoder - SRM 152, DIV 2, 250

	Passes all system tests.
"""

class FixedPointTheorem:
	def cycleRange(self, R):
		x = 0.25
		for i in xrange(0,2000000):
			x = R*x*(1.0-x)
		sample = []
		for i in xrange(0,1000):
			x = R*x*(1.0-x)
			sample.append(x)
		return max(sample)-min(sample)


tests = {
	0.0: [0.1],
	0.14754098360655865: [3.05],
}
c = FixedPointTheorem()
fail = False
for t in tests:
	res = c.cycleRange(*tests[t])
	ans = t
	if res != ans:
		fail = True
		print tests[t], res
if fail:
	print 'FAIL'
else:
	print 'PASS'
