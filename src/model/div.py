from .element import Element

class DivElement(Element):
	def __init__(self,soup,suffix='') -> None:
		super().__init__(soup)
		self.suffix = suffix
		self.ch = []
		# print('name of soup: ',soup.name)
		
		for child in soup.children:
			if child.name == None:
				from .span import SpanElement
				self.ch.append(SpanElement(child))
			else:	
				from .factory import get_element
				# print('type of child: ',type(child))
				# print("child's name: ",child.name)
				# print('child\'s content: ',child.prettify())
				# print("---")
				assert type(child) == type(soup), 'type of child: '+ str(type(child))
				self.ch.append(get_element(child))
			assert self.ch[-1] != None, 'child is None'

	def md(self) -> str:
		ret = ''
		for child in self.ch:
			ret += child.md()+''
		ret+=self.suffix
		return ret