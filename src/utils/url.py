from urllib.parse import quote

def encode_url(url_text):
	return quote(url_text)