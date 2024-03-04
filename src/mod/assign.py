import os
from bs4 import BeautifulSoup
from .base import Base
class Assign(Base):

	def __init__(self, title, link, out_dir):
		super().__init__(title, link, out_dir)
	
	
	def modify_page(self, x):
		# remove the last row containig submission comments
		element = x.find('tr', {'class': ['lastrow']})
		if element is not None:
			element.decompose()
		

	
		