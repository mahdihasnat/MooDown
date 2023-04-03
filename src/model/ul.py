from .element import Element

class UlElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		self.ch = []
		assert self.soup.name == 'ul'

		for child in self.soup.children:
			from .factory import get_element
			assert child.name == 'li', 'UlElement can only have li children but got: ' + child.name + ' instead'
			from .div import DivElement
			self.ch.append(DivElement(child))
		
	
	def md(self):
		s = ''
		for child in self.ch:
			s += '- ' + child.md() + '\n'
		return s