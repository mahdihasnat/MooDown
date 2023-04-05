
from .element import Element

class SpanElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		
	def md(self):
		return self.soup.get_text()