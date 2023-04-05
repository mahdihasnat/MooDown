from .type import Type,get_type
from model.a import AElement

import os
import pickle

def save_state(visited, q):
	with open('visited.pickle','wb') as f:
		pickle.dump(visited, f)
	with open('q.pickle','wb') as f:
		pickle.dump(q, f)
		pass

def load_state(root):
	visited = dict()
	# check if visited.pickle exists
	if os.path.exists('visited.pickle'):
		with open('visited.pickle','rb') as f:
			visited = pickle.load(f)
	q = list()
	q.append(root)
	if os.path.exists('q.pickle'):
		with open('q.pickle','rb') as f:
			q = pickle.load(f)
	return visited, q

def crawl(root,u):

	visited, q = load_state(root)

	counter = 1
	while len(q) > 0:
		counter = counter + 1
		if counter % 10 == 0:
			save_state(visited, q)

		obj = q.pop()

		if obj.link in visited:
			continue

		visited[obj.link] = obj.out_dir

		print('crawling',obj.link, ' in ', obj.out_dir, ' with title ', obj.title)
		
		AElement.clear_instances()
		obj.crawl(u)

		links = AElement.get_instances()
		for a in links:

			href = a.href.strip()
			title  = a.title().strip()
			
			typ = get_type(href)

			if typ != Type.OTHER:
				head = u.session.head(href, allow_redirects=True)
				if head.status_code == 200:
					href = head.headers['Location'] if 'Location' in head.headers else href

			typ = get_type(href)

			nxt = None

			if typ == Type.COURSE_VIEW:
				from mod.course import Course
				nxt = Course(title,href,obj.out_dir)
				
			elif typ == Type.ASSIGN:
				from mod.assign import Assign
				nxt = Assign(title,href,obj.out_dir)
				
			elif typ == Type.FOLDER or typ == Type.PAGE:
				from mod.base import Base
				nxt = Base(title, href, obj.out_dir)

			elif typ == Type.FORUM_VIEW:
				from mod.forum_view import ForumView
				nxt = ForumView(title, href, obj.out_dir)

			elif typ == Type.FORUM_DISCUS:
				from mod.forum_discus import ForumDiscus
				nxt = ForumDiscus(title, href, obj.out_dir)

			elif typ == Type.DATA:
				from mod.data import Data
				nxt = Data(title, href, obj.out_dir)

			elif typ == Type.FILE or typ == Type.RESOURCE or typ == Type.THEME:
				# already done in head request
				# head = u.session.head(href, allow_redirects=True)
				if 'text/html' in head.headers['Content-Type'].split(';'):
					from .base import Base
					nxt = Base(title, href, obj.out_dir)
				else:
					from mod.file import File
					nxt = File(title, href, obj.out_dir, head)
			
			if nxt is not None:
				if nxt.link in visited:
					nxt.out_dir = visited[nxt.link]
				rel_dir = os.path.relpath(nxt.out_dir, obj.out_dir)
				from utils.url import encode_url
				a.href = encode_url(rel_dir)
				if nxt.link not in visited:
					q.append(nxt)
		obj.write()

