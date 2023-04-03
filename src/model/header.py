from .element import Element

class HeaderElement(Element):

	def __init__(self,soup) -> None:
		super().__init__(soup)
		tag = self.soup.name
		text = self.soup.text
		self.md_ = '#'*int(tag[1:]) + ' ' + text + '\n'

	def md(self) -> str:
		return self.md_