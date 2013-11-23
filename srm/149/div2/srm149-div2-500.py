""" 
	TopCoder - SRM 149, DIV 2, 500

	Passes all system tests.
"""
import array,bisect,collections,fractions,heapq,itertools,math,re,string 

class BigBurger:
	def maxWait(self, arrival, service):
		m, t = 0,0
		for p in xrange(len(arrival)):
			t = max(t, arrival[p])
			m = max(m, t-arrival[p])
			t += service[p]
		return m

tests = {
	11: [[3,3,9],[2,15,14]],
}
c = BigBurger()
for t in tests:
	res = c.maxWait(*tests[t])
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL', res
