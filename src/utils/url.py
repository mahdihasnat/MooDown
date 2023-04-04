from hyperlink import parse


def encode_url(url_text):
	url_text = url_text.replace(':', '%3A')
	return parse(url_text,decoded = False).to_text()