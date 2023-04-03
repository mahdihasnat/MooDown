from .element import Element

class BElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		from .div import DivElement
		self.div = DivElement(soup)

	def md(self):
		return '**'+self.div.md()+'**'