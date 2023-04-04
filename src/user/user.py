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
