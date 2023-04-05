from .element import Element

class StrikeElement(Element):
	def __init__(self,soup) -> None:
		super().__init__(soup)
		from .div import DivElement
		self.div = DivElement(self.soup)

	def md(self) -> str:
		return '<strike>' + self.div.md() + '</strike>'