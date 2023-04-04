from enum import Enum
import sys
sys.path.append("..")
from config.settings import baseurl

class Type(Enum):
	ASSIGN = 1
	FORUM_VIEW = 2
	FORUM_DISCUS = 3
	RESOURCE = 4
	URL = 5
	OUT = 6
	FOLDER = 7
	PAGE = 8
	FILE = 9
	DATA = 10

def get_type(url):
	"""
		return type of url of moodle
	"""
	if baseurl+'mod/assign/' in url:
		return Type.ASSIGN
	elif baseurl+'mod/forum/view.php' in url:
		return Type.FORUM_VIEW
	elif baseurl+'mod/forum/discuss.php' in url:
		return Type.FORUM_DISCUS
	elif baseurl+'mod/resource/' in url:
		return Type.RESOURCE
	elif baseurl+'mod/url/' in url:
		return Type.URL
	elif baseurl+'mod/folder' in url:
		return Type.FOLDER
	elif baseurl+'mod/page' in url:
		return Type.PAGE
	elif baseurl+'pluginfile.php' in url:
		return Type.FILE
	elif baseurl+'mod/data/' in url:
		return Type.DATA
	elif baseurl in url:
		assert False, f'unknown url {url}'
	else:
		print("url is out of moodle: ", url)
		return Type.OUT