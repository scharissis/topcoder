"""
	TopCoder - SRM 146, DIV 2, 250

	Passes all system tests.
"""

class YahtzeeScore:
	def maxPoints(self, toss):
		m = 0
		for v in set(toss):
			m = max(m, sum([x for x in toss if x==v]))
		return m


tests = {
	5: [2,2,3,5,4],
	8: [5,4,4,3,6],
}
c = YahtzeeScore()
for t in tests:
	dice = tests[t]
	res = c.maxPoints(dice)
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL'
