from .base import Base
import os
from tqdm import tqdm
class File(Base):

	def __init__(self, title, link, out_dir, head) -> None:
		super().__init__('file', link, out_dir)

		file_name = self.get_file_name(head.headers['Content-Disposition'])
		self.out_dir = os.path.join(self.out_dir, file_name)
		self.title = title

	def get_file_name(self,headers_content_disposition):
		return headers_content_disposition.split(';')[1].split('=')[1].strip('"')
	
	def get_existing_file_size(self, out_dir):
		if os.path.exists(out_dir):
			return os.path.getsize(out_dir)
		return 0


	def crawl(self, u):
		r = u.session.get(self.link, stream=True)
		# print('link: ',self.link)
		total_size_in_bytes= int(r.headers.get('content-length', 0))
		block_size = 1024 #1 Kibibyte
		progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
		if self.get_existing_file_size(self.out_dir) == total_size_in_bytes:
			progress_bar.close()
			return
		with open(self.out_dir, 'wb') as f:
			for data in r.iter_content(block_size):
				progress_bar.update(len(data))
				f.write(data)
		progress_bar.close()
		if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
			print('WARNING: total size does not match progress bar size')
			print('p bar n: ',progress_bar.n)
			print('total size: ',total_size_in_bytes)
			print('link: ',self.link)
			print('out dir: ',self.out_dir)
			# assert False

	def write(self):
		pass
