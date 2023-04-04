# import required module
import sys
import os

# append the path of the
# parent directory
sys.path.append("..")

from config.settings import baseurl
from config.settings import id,pwd,local_output_dir
from requests import session

class User:
	
	def __init__(self,user,pwd) -> None:
		authdata = {
			'action': 'login',
			'username': user,
			'password': pwd
		}
		self.session = session()
		self.session.post(baseurl + 'login/index.php', data=authdata)
		assert self.session.get(baseurl + 'my/').status_code == 200
	
	def get(self, url):
		return self.session.get(baseurl + url)
	
	def get_absolute(self, url):
		return self.session.get(url)

if __name__ == '__main__':
	print('id: ',id)
	# print('pwd: ',pwd)
	u = User(id,pwd)
	from mod.dash import Dash
	root = Dash('',baseurl+'my/index.php?mynumber=-2',local_output_dir)
	from mod.crawler import crawl
	crawl(root,u)
