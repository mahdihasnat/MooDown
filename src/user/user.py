# import required module
import sys
import os

# append the path of the
# parent directory
sys.path.append("..")

from config.settings import baseurl
from config.settings import id,pwd,local_output_dir
from requests import session
from bs4 import BeautifulSoup

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
	
	def get_absolute_soup(self, url):
		r = self.session.get(url)
		assert r.status_code == 200
		s = BeautifulSoup(r.text,'html.parser')
		return s
