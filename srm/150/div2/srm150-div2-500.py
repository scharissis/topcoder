"""
	TopCoder - SRM 150, DIV 2, 500

	Passes all system tests.
"""

class InterestingDigits:
	def digits(self, base):
		interesting = []
		for d in range(2,base):
			if base%d==1:
				interesting.append(d)
		return tuple(interesting)


tests = {
	10: tuple([3,9]),
	3: tuple([2]),
	9: tuple([2,4,8]),
}

c = InterestingDigits()
fail = False
for t in tests:
	res = c.digits(t)
	ans = tests[t]
	if res != ans:
		fail = True
if fail:
	print 'FAIL'
else:
	print 'PASS'
