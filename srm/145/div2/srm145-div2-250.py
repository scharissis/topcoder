"""
	TopCoder - SRM 145, DIV 2, 250

	Passes all system tests.
"""

class ImageDithering:
	def count(self, dithered, screen):
		count = 0
		for row in screen:
			for c in row:
				if c in dithered:
					count +=1
		return count
		
		
tests = {
	24: {"BW":
		["AAAAAAAA",
		 "ABWBWBWA",
		 "AWBWBWBA",
		 "ABWBWBWA",
		 "AWBWBWBA",
		 "AAAAAAAA"]
	},
}

imd = ImageDithering()
for t in tests:
	d = tests[t].keys()[0]
	s = tests[t][d]
	res = imd.count(d,s)
	if res != t:
		print 'FAIL'
	else:
		print 'PASS'
