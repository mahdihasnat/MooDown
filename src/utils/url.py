from urllib.parse import quote

def encode_url(url_text):
	splits = url_text.split(':')
	return ':'.join([quote(t) for t in splits])