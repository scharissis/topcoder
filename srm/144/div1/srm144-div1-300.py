"""
	TopCoder 
	SRM 144 DIV 1 - 300

	Passed all system tests.
	Submitted for 90.00 points.

	Binary messages are encrypted p --> q as such:
		q[n] = p[n-1] + p[n] + p[n+1]
	Decode them.
"""

class BinaryCode:
	def decode(self, message):
		none = "NONE"
		q = [int(l) for l in message]	# encypted digits
		decrypted = [none,none]
		for first in (0,1):
			res = []
			res .append(first)
			invalid = False
			i = 1
			for d in q[:-1]:
				val = d - res[i-1]
				if i >= 2:
					val -= res[i-2]
				if val not in (0,1):
					invalid = True
					break
				res.append(val)
				i += 1
			if invalid:
				decrypted[first] = none
			else:
				# quick validity check for last digit
				if sum(res[-2:]) != int(message[-1]):
					res = [none]
				decrypted[first] = ''.join([str(x) for x in res])
		return tuple(decrypted)

# encrypted, plaintext
tests = {
	"123210122": ("011100011", "NONE"),
	"123210120": ("NONE", "NONE"),
	"3": ("NONE", "NONE"),
}
d = BinaryCode()
for t in tests:
	r = d.decode(t)
	a = tests[t]

	status = 'FAIL'
	if r == a:
		status = 'PASS'
	else:
		status = 'FAIL'
	print '[{0}] {1} --> {2}'.format(status, t, r)
