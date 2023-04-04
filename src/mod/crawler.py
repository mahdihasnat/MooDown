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
	visited = set()
	# check if visited.pickle exists
	if os.path.exists('visited.pickle'):
		with open('visited.pickle','rb') as f:
			visited = pickle.load(f)
	q = []
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

		visited.add(obj.link)

		print('crawling',obj.link, ' in ', obj.out_dir)
		AElement.clear_instances()
		obj.crawl(u)

		links = AElement.get_instances()
		for a in links:

			href = a.href.strip()
			title  = a.title().strip()
			typ = get_type(href)

			nxt = None

			if typ == Type.COURSE_VIEW:
				from mod.course import Course
				nxt = Course(title,href,obj.out_dir)
				
			elif typ == Type.ASSIGN:
				from mod.assign import Assign
				nxt = Assign(title,href,obj.out_dir)
				
			elif typ == Type.FOLDER:
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
			
			
			if nxt is not None:
				rel_dir = os.path.relpath(nxt.out_dir, obj.out_dir)
				from utils.url import encode_url
				a.href = encode_url(rel_dir)
				q.append(nxt)
		obj.write()

