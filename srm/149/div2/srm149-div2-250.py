""" 
	TopCoder - SRM 149, DIV 2, 250

	Passes all system tests.
"""
import array,bisect,collections,fractions,heapq,itertools,math,re,string 

class FormatAmt:
	def amount(self, dollars, cents):
		a = round((cents+dollars*100)/100.,2)
		return '${:,.02f}'.format(a)

tests = {
	"$123,456.00": [123456,0],
}
c = FormatAmt()
for t in tests:
	res = c.amount(*tests[t])
	ans = t
	if res == ans:
		print 'PASS'
	else:
		print 'FAIL', res
