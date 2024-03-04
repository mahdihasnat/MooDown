from enum import Enum
import sys
sys.path.append("..")
from config.settings import baseurl

class Type(Enum):
	ASSIGN = 1
	FOLDER = 2
	PAGE = 3
	DATA = 4
	FILE = 5
	FORUM_VIEW = 6
	FORUM_DISCUS = 7
	FORUM_OTHER = 8
	RESOURCE = 9
	URL = 10
	COURSE_VIEW = 11
	USER_VIEW = 12
	THEME = 13
	QUIZ =14
	OTHER = 15


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
	elif baseurl+'theme/' in url:
		return Type.THEME
	elif baseurl+'mod/quiz' in url:
		return Type.QUIZ
	elif baseurl in url:
		assert False, f'unknown url {url}'
	else:
		print("url is out of moodle: ", url)
		return Type.OTHER