import os
from bs4 import BeautifulSoup
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
		r = u.get_absolute(self.link)
		assert r.status_code == 200
		s = BeautifulSoup(r.text,'html.parser')
		x = s.find('div',{'role':'main'})
		from model.factory import get_element
		t = get_element(x)
		with open(os.path.join(self.out_dir,'README.md'),'w') as f:
			f.write(t.md())
		