import os
import sys
 
# append the path of the
# parent directory
sys.path.append("..")

from bs4 import BeautifulSoup

class Course:

	def __init__(self, title, link, out_dir) -> None:
		
		# if out_dir doesnot exist, create it

		term, courseid, coursetitle = self.get_term_courseid_coursetitle(title)

		out_dir = os.path.join(out_dir, term)
		out_dir = os.path.join(out_dir, courseid)
		
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		assert os.path.exists(out_dir), f'out_dir {out_dir} doesnot exist'

		self.link = link
		self.out_dir = out_dir
		self.title = title
	
	def crawl(self,u):
		from model.a import AElement
		AElement.clear_instances()
		from model.factory import get_element

		r = u.get_absolute(self.link)
		assert r.status_code == 200
		b = BeautifulSoup(r.text, 'html.parser')
		root = b.find('div',class_ = 'course-content')
		elem = get_element(root)
		readme = elem.md()
		with open(os.path.join(self.out_dir, 'README.md'), 'w') as f:
			f.write(readme)
		


	def get_term_courseid_coursetitle(self,title):
		s = title.split(' ')
		term = ' '.join(s[:2])
		courseid = s[2][:-1]
		coursetitle = ' '.join(s[3:])
		return term, courseid, coursetitle
