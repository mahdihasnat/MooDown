from .element import Element

class PreElement(Element):

	def __init__(self, soup) -> None:
		super().__init__(soup)
	
	def md(self):
		return '```\n'+self.soup.get_text()+'\n```\n'