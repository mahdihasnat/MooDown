from .element import Element

class OlElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		self.ch = []
		assert self.soup.name == 'ol'

		for child in self.soup.children:
			from .factory import get_element
			assert child.name == 'li', 'UlElement can only have li children but got: ' + child.name + ' instead'
			from .div import DivElement
			self.ch.append(DivElement(child))
		
	
	def md(self):
		s = ''
		count = 1
		for child in self.ch:
			s += str(count)+' ' + child.md() + '\n'
			count +=1
		return s