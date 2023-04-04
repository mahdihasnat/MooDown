from .base import Base

class ForumDiscus(Base):

	def __init__(self, title, link, out_dir):
		super().__init__(title, link, out_dir)
	

	def modify_page(self, x):
		# remove the select box
		x.find('div',{'class':['discussioncontrols', 'clearfix']}).decompose()

		# remove row side , which contains show parent and reply
		y = x.find_all('div',{'class':['side']})
		for i in y:
			i.decompose()