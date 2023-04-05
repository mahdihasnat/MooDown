from .element import Element

from urllib.parse import parse_qs
def get_image_title(link):
	try:
		y = parse_qs(link)['image'][0]
	except:
		assert False
		y='img'
	return y

class ImgElement(Element):
	def get_soup_of_link(self,link,title):
		from bs4 import BeautifulSoup
		return BeautifulSoup('<a href="' + link + '"> '+title+' </a>','html.parser').a

	def __init__(self, soup) -> None:
		super().__init__(soup)
		assert self.soup.name == 'img'
		from .a import AElement
		title = self.soup['title'] if 'title' in self.soup.attrs else get_image_title(self.soup['src'])
		s = self.get_soup_of_link(self.soup['src'],title)
		self.a = AElement(s)

	def md(self):
		self.soup.attrs['src'] = self.a.href
		ret = '<img ' + ' '.join([str(k) + '="' + str(v) + '"' for k,v in self.soup.attrs.items()]) + ' />'
		return ret
	
	def text(self):
		return ''