from .element import Element

class ImgElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		assert self.soup.name == 'img'

	def md(self):
		return ''