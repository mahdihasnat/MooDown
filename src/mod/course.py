import os
import sys
 
# append the path of the
# parent directory
sys.path.append("..")

from bs4 import BeautifulSoup
from .base import Base

class Course(Base):

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

		print(f'crawling {self.link}...')

		from model.a import AElement
		AElement.clear_instances()
		from model.factory import get_element

		b = u.get_absolute_soup(self.link)
		root = b.find('div',class_ = 'course-content')
		self.model = get_element(root)
	
	def get_term_courseid_coursetitle(self,title):
		s = title.split(' ')
		term = ' '.join(s[:2])
		courseid = s[2][:-1]
		coursetitle = ' '.join(s[3:])
		return term, courseid, coursetitle
