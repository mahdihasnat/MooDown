from .base import Base

class ForumView(Base):

	def __init__(self, title, link, out_dir):
		super().__init__(title, link, out_dir)
	

	def modify_page(self, x):

		y = x.find_all('td', {'class':'replies'})
		assert y!=None

		for i in y:
			try:
				i.find('a').unwrap()
			except:
				pass
		y = x.find_all('td', {'class':'lastpost'})
		assert y!=None

		for i in y:
			for j in i.find_all('a'):
				j.unwrap()
			
		