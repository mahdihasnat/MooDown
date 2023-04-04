import os

class Assign:

	def __init__(self, title, link, out_dir):
		out_dir = os.path.join(out_dir, title)
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		assert os.path.exists(out_dir), f'out_dir {out_dir} doesnot exist'

		self.link = link
		self.out_dir = out_dir
		self.title = title
	
	def crawl(self,u):
		pass