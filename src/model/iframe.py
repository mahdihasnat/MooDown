from .element import Element


class IframeElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)

		self.text = soup['title']
		self.href = soup['src']

	def md(self):
		return f'[{self.text}]({self.href})'