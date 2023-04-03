from .element import Element

class DivElement(Element):
	def __init__(self,soup) -> None:
		super().__init__(soup)
		self.ch = []
		# print('name of soup: ',soup.name)
		
		for child in soup.children:
			from .factory import get_element
			# print('type of child: ',type(child))
			self.ch.append(get_element(child))
		
	def md(self) -> str:
		ret = ''
		for child in self.ch:
			ret += child.md()+' '
		return ret