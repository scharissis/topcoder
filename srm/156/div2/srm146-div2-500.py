"""
	TopCoder - SRM 146, DIV 2, 500
"""

class RectangularGrid:
	def countRectangles(self, width, height):
		count = 0
		for w in xrange(1, width+1):
			for h in xrange(1, height+1):
				if w == h: continue
				count += (width-w+1) * (height-h+1)
		return count


# answer: question
tests = {
	22: [3,3],
	31: [5,2],
	2640: [10,10],
	84850147296: [900,647],
}
c = RectangularGrid()
for t in tests:
	res = c.countRectangles(*tests[t])
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL', tests[t], res
