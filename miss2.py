class shape:
	def __init__(self,w,l):
		self.width = w
		self.len = l
	def print_size(self):
		print("{}by{}".format(self.width, self.len))

class square(shape):
	pass

a_sq = square(20, 25)
a_sq.print_size()
print("git")