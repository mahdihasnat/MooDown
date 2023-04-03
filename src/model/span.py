
from .element import Element

class SpanElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		self.md_ = soup.text
		# print('in span: ',soup.name)
		# print('content:',soup.text)
	def md(self):
		return self.md_