from enum import Enum
import sys
sys.path.append("..")
from config.settings import baseurl

class Type(Enum):
	ASSIGN = 1
	FOLDER = 7
	PAGE = 8
	DATA = 10
	FILE = 9
	FORUM_VIEW = 2
	FORUM_DISCUS = 3
	FORUM_OTHER = 4
	RESOURCE = 5
	URL = 6
	COURSE_VIEW = 11
	USER_VIEW = 12
	OTHER = 13


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
	elif baseurl+'mod/forum/' in url:
		return Type.FORUM_OTHER
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
	elif baseurl+'course/view.php' in url:
		return Type.COURSE_VIEW
	elif baseurl+'user/view.php' in url:
		return Type.USER_VIEW
	elif baseurl in url:
		assert False, f'unknown url {url}'
	else:
		print("url is out of moodle: ", url)
		return Type.OTHER