from .element import Element

class AElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		assert self.soup.name == 'a'
		self.href = self.soup['href']
		from .factory import get_element
		from .div import DivElement
		self.ch = DivElement(self.soup)

	def md(self):
		return '[' + self.ch.md() + '](' + self.href + ')'