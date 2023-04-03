from .div import DivElement
from .header import HeaderElement

def get_element(soup):
	# print("currently parsing: ",soup.name)
	# print("current content: ",soup.prettify())
	if soup.name == 'div':
		return DivElement(soup)
	elif soup.name[0] == 'h' and soup.name[1:].isdigit():
		return HeaderElement(soup)
	elif soup.name == 'ul':
		from .ul import UlElement
		return UlElement(soup)
	elif soup.name == 'img':
		from .img import ImgElement
		return ImgElement(soup)
	elif soup.name == 'a':
		from .a import AElement
		return AElement(soup)
	elif soup.name == 'span':
		from .span import SpanElement 
		return SpanElement(soup)
	else:
		# print(soup.contents)
		# for child in soup.children:
		# 	print(child.name)
		# 	for c in child.children:
		# 		print(c.name)
		# 	print('--')
		assert False, 'Unknown element type: ' + soup.name