from .element import Element

class WbrElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)

	def md(self):
		return ' '