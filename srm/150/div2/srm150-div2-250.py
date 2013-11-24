"""
	TopCoder - SRM 150, DIV 2, 250

	Passes all system tests.
"""

class WidgetRepairs:
	def days(self, arrivals, numPerDay):
		arrivals = list(arrivals)
		extras = 0
		count = 0
		for i in xrange(0, len(arrivals)):
			if arrivals[i] > 0:
				count += 1
			rem = arrivals[i] - numPerDay
			if rem > 0:
				if i+1 < len(arrivals):
					arrivals[i+1] += rem
				else:
					extras += rem
		while extras > 0:
			extras -= numPerDay
			count += 1
		return count


tests = {
	6: [tuple([10,0,0,4,20]),8],
	0: [tuple([0,0,0]),10],
	20: [tuple([100,100]),10],
	4: [tuple([27,0,0,0,0,9]),9],
}

c = WidgetRepairs()
fail = False
for t in tests:
	res = c.days(*tests[t])
	ans = t
	if res != t:
		fail = True
		print tests[t], res
if fail:
	print 'FAIL'
else:
	print 'PASS'
