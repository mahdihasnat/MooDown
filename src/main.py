from user.user import User
from config.settings import baseurl
from config.settings import id,pwd,local_output_dir

if __name__ == '__main__':
	print('id: ',id)
	# print('pwd: ',pwd)
	print('local_output_dir: ',local_output_dir)
	u = User(id,pwd)
	from mod.dash import Dash
	root = Dash('',baseurl+'my/index.php?mynumber=-2',local_output_dir)
	from mod.crawler import crawl
	crawl(root,u)
