from .div import DivElement
from .header import HeaderElement

def get_element(soup):
	# print("current parsing: ",soup.name)
	# print("current content: ",soup.prettify())
	if soup.name in ['div','textarea','font','form']:
		return DivElement(soup)
	elif soup.name[0] == 'h' and soup.name[1:].isdigit():
		from .html import HtmlElement
		return HtmlElement(soup)
		# return HeaderElement(soup)
	# elif soup.name == 'ul':
	# 	from .ul import UlElement
	# 	return UlElement(soup)
	elif soup.name == 'ol':
		from .ol import OlElement
		return OlElement(soup)
	elif soup.name == 'img':
		from .img import ImgElement
		return ImgElement(soup)
	elif soup.name == 'a':
		from .a import AElement
		return AElement(soup)
	elif soup.name == 'p':
		from .p import PElement
		return PElement(soup)
	elif soup.name == 'b':
		from .b import BElement
		return BElement(soup)
	elif soup.name == 'i':
		from .i import IElement
		return IElement(soup)
	elif soup.name == 'u':
		return DivElement(soup)
	elif soup.name == 'strike':
		from .strike import StrikeElement
		return StrikeElement(soup)
	elif soup.name == 'br':
		from .br import BrElement
		return BrElement(soup)
	elif soup.name == 'wbr':
		from .wbr import WbrElement
		return WbrElement(soup)
	elif soup.name == 'span':
		return DivElement(soup)
	elif soup.name == 'iframe':
		from .iframe import IframeElement
		return IframeElement(soup)
	elif soup.name == 'google-sheets-html-origin':
		return DivElement(soup)
	elif soup.name in ['table','tbody','tr','td','ul','li']:
		from .html import HtmlElement
		return HtmlElement(soup)
	elif soup.name in ['input']:
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