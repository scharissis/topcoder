"""
	TopCoder - SRM 598, DIV 2, 250
	
	Passes all system tests.
"""

class ErasingCharacters:
	def simulate(self, s):
		while True:
			ok = True 
			for i in xrange(len(s)-1):
				if s[i] == s[i+1]:
					s = s[:i] + s[i+2:]
					ok = False
					break
			if ok: break
		return s

tests = {
	"cl": "cieeilll",
	"topcoder": "topcoder",
}
c = ErasingCharacters()
for t in tests:
	ans = t
	q = tests[t]
	res = c.simulate(q)
	if res != ans:
		print 'FAIL', res
	else:
		print 'PASS'	
