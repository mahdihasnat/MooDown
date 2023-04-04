from .div import DivElement
from .header import HeaderElement

def get_element(soup):
	# print("current parsing: ",soup.name)
	# print("current content: ",soup.prettify())
	
	if soup.name == 'div':
		return DivElement(soup,'\n')
	elif soup.name in ['textarea','font','form']:
		return DivElement(soup)
	elif soup.name[0] == 'h' and soup.name[1:].isdigit():
		from .html import HtmlElement
		return HtmlElement(soup)
	elif soup.name == 'img':
		from .img import ImgElement
		return ImgElement(soup)
	elif soup.name == 'a':
		if soup.has_attr('href'):
			from .a import AElement
			return AElement(soup)
		else:
			from .html import HtmlIgnoreElement
			return HtmlIgnoreElement(soup)
	elif soup.name in ['p','label']:
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
	elif soup.name in ['strike','s']:
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
	elif soup.name in ['table','thead','th','tbody','tr','td','ul','li','ol',
				'col','colgroup','center']:
		from .html import HtmlElement
		return HtmlElement(soup)
	elif soup.name in ['input']:
		from .span import SpanElement
		return SpanElement(soup)
	elif soup.name in ['pre']:
		from .pre import PreElement
		return PreElement(soup)
	elif soup.name in ['sub','sup']: # ignore subscript and superscript
		return DivElement(soup)
	elif soup.name in ['hr']:
		from .html import HtmlSingleton
		return HtmlSingleton(soup)
	elif soup.name in ['param','object','video','source']:
		from .html import HtmlIgnoreElement
		return HtmlIgnoreElement(soup)
	else:
		# print(soup.contents)
		# for child in soup.children:
		# 	print(child.name)
		# 	for c in child.children:
		# 		print(c.name)
		# 	print('--')
		assert False, 'Unknown element type: ' + soup.name