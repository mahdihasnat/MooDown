from .element import Element	


class HtmlElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		self.chs = []
		for ch in soup.children:
			if ch.name == None:
				from .span import SpanElement
				self.chs.append(SpanElement(ch))
			else:	
				from .factory import get_element
				# print("name child: ",ch.name)
				self.chs.append(get_element(ch))
			
		
	def md(self):
		ret ='<'+self.soup.name+'>'
		for ch in self.chs:
			ret += ch.md()
		ret += '</'+self.soup.name+'>'
		return ret
	
	def text(self):
		ret = ''
		for ch in self.chs:
			ret += ch.text()
		return ret

class HtmlSingleton(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
	
	def md(self):
		return '<'+self.soup.name+' />'

class HtmlIgnoreElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
		self.chs = []
		for ch in soup.children:
			if ch.name == None:
				from .span import SpanElement
				self.chs.append(SpanElement(ch))
			else:	
				from .factory import get_element
				self.chs.append(get_element(ch))

	def md(self):
		ret = ''
		for ch in self.chs:
			ret += ch.md()
		return ret
