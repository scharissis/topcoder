"""
	TopCoder - SRM 145, DIV 2, 500

	Passes all system tests.
"""

class ExerciseMachine:
	def getPercentages(self, time):
		h, m, s = map(int, time.split(':')[0:3])
		seconds = h*3600 + m*60 + s
		count = 0
		lc = 0 # multiples of lowest used to avoid rounding errors
		for i in xrange(1,100):
			tmp = seconds*(i/100.)
			if float(int(tmp)) == tmp:
				lc = tmp
				break
		if lc != 0:
			j = 1
			while tmp*j < seconds:
				count += 1
				j += 1
		return count 

em = ExerciseMachine()
tests = {
	99: "00:30:00",
	19: "00:28:00",
	0: "23:59:59",
}
for t in tests:
	time = tests[t]
	if t != em.getPercentages(time):
		print 'FAIL - got', em.getPercentages(time), 'expected', t, '[', time, ']'
	else:
		print 'PASS'
