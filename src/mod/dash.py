from .base import Base

class Dash(Base):

	def __init__(self, title, link, out_dir) -> None:
		super().__init__(title, link, out_dir)

	
	def modify_page(self, x):
		x.find('aside').unwrap()
		x.find('a',{'class':'skip-block'}).unwrap()
		
		while True:
			try:
				x.find('div',{'class':'activity_info'}).decompose()
			except:
				break