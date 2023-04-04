from .base import Base

class ForumDiscus(Base):

	def __init__(self, title, link, out_dir):
		super().__init__(title, link, out_dir)
	

	def modify_page(self, x):
		# remove the select box
		x.find('div',{'class':['discussioncontrols', 'clearfix']}).decompose()

		# with open('tmp.html','w') as f:
		# 	f.write(x.prettify())