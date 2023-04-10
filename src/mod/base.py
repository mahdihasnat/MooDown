import os
from bs4 import BeautifulSoup
from sanitize_filename import sanitize
class Base():

	def __init__(self, title, link, out_dir) -> None:
		if title != '':
			title = sanitize(title)
			# print(f'crawling {title}')
			out_dir = os.path.join(out_dir, title)
		
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		
		# assert os.path.exists(out_dir), f'out_dir {out_dir} doesnot exist'

		self.link = link
		self.out_dir = out_dir
		self.title = title

	
	def modify_page(self, x):
		pass

	def crawl(self, u):
		s = u.get_absolute_soup(self.link)
		x = s.find('div',{'role':'main'})

		self.modify_page(x)
		
		from model.factory import get_element
		self.model = get_element(x)
	
	def write(self):
		readme = self.model.md()
		with open(os.path.join(self.out_dir,'README.md'),'w', encoding='utf-8') as f:
			f.write(readme)
