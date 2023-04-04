# import required module
import sys
import os
from dotenv import load_dotenv
load_dotenv()
 
# append the path of the
# parent directory
sys.path.append("..")

from config.settings import baseurl
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
	
	def get_courses(self):
		r = self.get('my/index.php?mynumber=-2')
		assert r.status_code == 200

		from bs4 import BeautifulSoup
		soup = BeautifulSoup(r.text, 'html.parser')

		course_dict = dict()

		all_course = soup.find('div',class_ ='course_list').find_all('div',class_ ='course_title')

		for c in all_course:
			course_box = c.find('h2',class_ = 'title').find('a')
			c_link = course_box.get('href')
			c_title = course_box.get('title')
		#             print(c_link)
		#             print(c_title)
			course_dict[c_title] = c_link
		# print(course_dict)
		return course_dict

	def crawl(self, out_dir):
		course_dict = self.get_courses()
		self.courses = []
		from course.course import Course
		for title, link in course_dict.items():
			self.courses.append(Course(title, link, out_dir))
		
		for c in self.courses[0:]:
			c.crawl(self)


if __name__ == '__main__':
	id = os.environ.get('moodle_id')
	print("id: ",id)
	print("id type",type(id))
	pwd = os.environ.get('moodle_pwd')
	# print("pwd: ",pwd)
	local_output_dir = os.environ.get('local_output_dir')
	u = User(id,pwd)
	u.crawl(local_output_dir)