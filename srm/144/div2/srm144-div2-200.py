"""
	TopCoder - SRM 144, DIV 2, 200

	Passes all system tests.
	
	Submitted for 90 points.
"""

class Time:
	def whatTime(self, seconds):
		hrs = 60**2
		mins = 60
		h = int(seconds // hrs)
		m = int(seconds%hrs // mins)
		s = int(seconds%hrs%mins)
		return '{0}:{1}:{2}'.format(h,m,s)
		

tests = {
	0: "0:0:0",
	3: "0:0:3",
	63: "0:1:3",
	5436: "1:30:36",
}
time = Time()
for t in tests:
	print t, '-->', time.whatTime(t)
		
