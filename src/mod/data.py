from .base import Base

class Data(Base):
	def __init__(self, title, link, out_dir) -> None:
		super().__init__(title, link, out_dir)
	
	def modify_page(self, x):
		
		
		# remove navigation bar
		x.find('ul', {'class': 'nav-tabs'}).decompose()

		
