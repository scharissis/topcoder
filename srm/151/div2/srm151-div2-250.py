"""
	TopCoder - SRM 151, DIV 2, 250

	Passes all system tests.
"""

class PrefixCode:
	def isOne(self, words):
		w_set = set()
		for w in words:
			w_set.add(w)
		if len(w_set) == 1:
			return "Yes"
		for w in words:
			for p in w_set:
				if w.startswith(p):
					return "No, "+str(words.index(p))
		return "Yes"


tests = {
	"Yes": [['trivial']],
	"No, 0": [['bad', 'badass']],
	"No, 2": [['10001', '011', '100', '100', '10']],
	"No, 0": [['no', 'nosy', 'neighbours', 'needed']],
}
c = PrefixCode()
fail = False
for t in tests:
	res = c.isOne(*tests[t])
	ans = t
	if res != ans:
		fail = True
		print tests[t], res
if fail:
	print 'FAIL'
else:
	print 'PASS'
