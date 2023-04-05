from .element import Element

class AElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		assert self.soup.name == 'a'
		try:
			self.href = self.soup['href']
		except:
			self.href = ''
		
		from .factory import get_element
		from .div import DivElement
		self.ch = DivElement(self.soup)

	def md(self):
		return '<a href="' + self.href + '">' + self.ch.text().strip() + '</a>'
	
	def title(self):
		return self.ch.text()