""" 
	TopCoder - SRM 148, DIV 2, 600

	Passes system tests.
"""
import array,bisect,collections,fractions,heapq,itertools,math,re,string 

class CeyKaps:
	def decipher(self, typed, switches):
		deciphered = ''.join([x for x in typed])
		
		# Create a dict with 2 entries, for each switch.
		dicts = []
		for s in switches:
			a,b = s.split(':')[0:2]
			d = {a:b,b:a}
			dicts += [d]

		# For each dict, perform both switches _concurrently_.
		for d in dicts:
			tmp = [x for x in deciphered]
			swaps = {}
			for s in d:
				for i, l in enumerate(tmp):
					if l == s:
						if s in swaps:
							swaps[s] += [i]
						else:
							swaps[s] = [i]
			for s in swaps:
				for e in swaps[s]:
					tmp[e] = d[s]
			deciphered = ''.join(tmp)

		return deciphered 

tests = {
	"CCCCC": ["AAAAA", ["A:B", "B:C", "A:D"]],
	"AEBCD": ["ABCDE", ["A:B", "B:C", "C:D", "D:E", "E:A"]],
	"WHOSWITCHEDMYKEYCAPSAROUND": ["IHWSIOTCHEDMYKEYCAPSARWUND", ["W:O", "W:I"]],
}
c = CeyKaps()
for t in tests:
	p = tests[t]
	res = c.decipher(*p)
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL', p, 'returned', res
