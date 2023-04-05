from .base import Base
import os

class File(Base):

	def __init__(self, title, link, out_dir, head) -> None:
		super().__init__('file', link, out_dir)

		file_name = self.get_file_name(head.headers['Content-Disposition'])
		self.out_dir = os.path.join(self.out_dir, file_name)
		self.title = title

	def get_file_name(self,headers_content_disposition):
		return headers_content_disposition.split(';')[1].split('=')[1].strip('"')
	
	def crawl(self, u):
		r = u.session.get(self.link, stream=True)
		print("out_dir: ",self.out_dir)
		with open(self.out_dir, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024):
				if chunk:
					f.write(chunk)

	def write(self):
		pass
