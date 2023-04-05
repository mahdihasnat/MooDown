
# we want to get all instance of subclass, say AElement
# https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class

from collections import defaultdict
import weakref

class Element:
	__refs__ = defaultdict(list)

	def __init__(self,soup) -> None:
		self.soup = soup
		self.__refs__[self.__class__].append(weakref.ref(self))
	
	@classmethod
	def get_instances(cls):
		ret = []
		for inst_ref in cls.__refs__[cls]:
			inst = inst_ref()
			if inst is not None:
				ret.append(inst)
		return ret
	
	@classmethod
	def clear_instances(cls):
		cls.__refs__[cls] = []

	def md(self):
		assert False, 'Not implemented'
	
	def text(self):
		return self.md()