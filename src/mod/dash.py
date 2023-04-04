from .base import Base

class Dash(Base):

	def __init__(self, title, link, out_dir) -> None:
		super().__init__(title, link, out_dir)

	
	def modify_page(self, x):
		x.find('aside').unwrap()
		
		# with open('tmp.html', 'w') as f:
		# 	f.write(x.prettify())